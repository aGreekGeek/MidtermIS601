'''app/__init__.py: Handles the application’s core flow.'''
import os
import pkgutil
import importlib
import sys
from typing import Type
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand
from dotenv import load_dotenv
import logging
import logging.config

class App:
    '''Primary class for the application.'''
    
    def __init__(self):  # Constructor
        os.makedirs('logs', exist_ok=True)
        self.setup_logging()
        load_dotenv()
        self.settings = self.fetch_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def setup_logging(self):
        log_config = 'logging.conf'
        if os.path.isfile(log_config):
            logging.config.fileConfig(log_config, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging setup complete.")

    def fetch_environment_variables(self):
        env_settings = {key: value for key, value in os.environ.items()}
        logging.info("Loaded environment variables.")
        return env_settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT', default_value=None):
        return self.settings.get(env_var, default_value)

    def load_plugins(self):
        '''Load plugins dynamically from app.plugins directory.'''
        plugin_directory = 'app.plugins'
        plugin_path = plugin_directory.replace('.', '/')
        if not os.path.isdir(plugin_path):
            logging.warning(f"Plugin directory '{plugin_path}' is missing.")
            return
        
        for _, plugin_name, is_package in pkgutil.iter_modules([plugin_path]):
            if is_package:
                try:
                    module = importlib.import_module(f'{plugin_directory}.{plugin_name}')
                    self.register_plugin_commands(module, plugin_name)
                except ImportError as err:
                    logging.error(f"Failed to import plugin '{plugin_name}': {err}")
                except Exception as err:
                    logging.error(f"Error while loading plugin '{plugin_name}': {err}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        '''Add commands from plugin modules.'''
        for attribute_name in dir(plugin_module):
            attribute = getattr(plugin_module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                # Register commands, excluding MenuCommand unless from "menu" plugin
                if plugin_name != "menu":
                    self.command_handler.register_command(plugin_name, attribute())
                    logging.info(f"Registered '{attribute_name}' from '{plugin_name}' plugin.")
                else:
                    # Specific registration for MenuCommand
                    self.command_handler.register_command(plugin_name, MenuCommand(self.command_handler))
                    logging.info(f"MenuCommand registered from '{plugin_name}' plugin.")

    def start(self):
        '''Initialize and run the application.'''
        self.load_plugins()
        logging.info("Application has started.")
        print("Welcome to the basic calculator.\n\tEnter 'menu' for a list of commands or 'exit' to close the app.")
        try:
            while True:  # REPL (Read, Evaluate, Print, Loop)
                user_input = input(">>> ").strip()
                if user_input.lower() == 'exit':
                    logging.info("User initiated application exit.")
                    sys.exit(0)  # Clean exit
                try:
                    self.command_handler.execute_command(user_input)
                except KeyError:  # Assuming KeyError for unknown commands
                    logging.error(f"Unrecognized command: {user_input}")
                    continue  # Prompt for input again
        except KeyboardInterrupt:
            logging.info("Application interrupted. Exiting cleanly.")
            sys.exit(0)  # Handle KeyboardInterrupt gracefully
        finally:
            logging.info("Application has shut down.")

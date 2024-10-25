import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from dotenv import load_dotenv
import logging
import logging.config
from app.plugins.history import HistoryMenuCommand

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
        '''
        Dynamically load all plugins from the app.plugins directory.
        '''
        plugin_directory = 'app.plugins'
        plugin_path = plugin_directory.replace('.', '/')
        
        # Discover all modules in the 'app.plugins' directory
        for _, plugin_name, _ in pkgutil.iter_modules([plugin_path]):
            try:
                # Import the module dynamically
                module = importlib.import_module(f'{plugin_directory}.{plugin_name}')
                # Check if the module has a `register_commands` function
                if hasattr(module, 'register_commands'):
                    # Register commands via the module's function
                    module.register_commands(self.command_handler)
                    logging.info(f"Successfully loaded plugin: {plugin_name}")
                else:
                    logging.warning(f"Plugin '{plugin_name}' does not have a 'register_commands' function.")
            except ImportError as err:
                logging.error(f"Failed to import plugin '{plugin_name}': {err}")

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

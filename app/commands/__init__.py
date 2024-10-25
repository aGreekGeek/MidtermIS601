from abc import ABC, abstractmethod
from typing import Dict
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        '''Defines the method that each cmd must implement'''
        pass  # pragma: no cover

class CommandHandler:
    _instance = None

    # Singleton Method for single instances
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CommandHandler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'commands'):
            self.commands: Dict[str, Command] ={}

        '''Manages the reg and execution of commands'''
        self.commands: Dict[str, Command]= {}

    def register_command(self, command_name: str, command: Command):
        '''registers command under the provided name'''
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        '''Executs the command under the name'''
        try:
            self.commands[command_name].execute()
            logging.info(f"Executed command: {command_name}")
        except KeyError:
            logging.error(f"No such command")
            print(f"No such command: {command_name}")
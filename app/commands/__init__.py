from abc import ABC, abstractmethod
from typing import Dict
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        '''Defines the method that each cmd must implement'''
        pass  # pragma: no cover

class CommandHandler:
    def __init__(self):
        '''Manages the reg and execution of commands'''
        self.commands: Dict[str, Command]= {}

    def register_command(self, command_name: str, command: Command):
        '''registers command under the provided name'''
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        '''Executs the command under the name'''
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
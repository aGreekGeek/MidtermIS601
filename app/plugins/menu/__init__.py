import sys
from app.commands import Command

class MenuCommand(Command):
    '''
    Command class responsible for displaying a list of available commands.

    This class generates and prints out a dynamic menu by checking the registered
    commands in the CommandHandler and showing them to the user.
    '''

    def __init__(self, command_handler):
        '''
        Constructor for MenuCommand, accepts a CommandHandler instance.

        Args:
        - command_handler (CommandHandler): The CommandHandler instance that manages command registration.
        '''
        self.command_handler = command_handler

    def execute(self):
        '''
        Executes the MenuCommand.

        This method prints the list of currently available commands to the console.
        '''
        print("Available Commands:")
        for command_name in self.command_handler.commands:
            print("\t-", command_name)
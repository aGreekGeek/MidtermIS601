import sys
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.add import AddCommand

class ExitCommand(Command):
    '''
    Command class for exiting the calculator application.

    Provides functionality to terminate the application when executed.
    '''

    def execute(self):
        '''
        Executes the ExitCommand.

        This method exits the calculator application with a farewell message.
        '''
        sys.exit("I hope you enjoyed my Calculator App. Have a great day!")


def register_commands(handler: CommandHandler):
    '''Registers ExitCommand with the command handler.'''
    handler.register_command('exit', ExitCommand())

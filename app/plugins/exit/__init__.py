import sys
from app.commands import Command

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
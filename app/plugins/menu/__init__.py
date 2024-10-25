from app.commands import Command, CommandHandler

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
            print(f"\t- {command_name}")

class HelpCommand(Command):
    '''
    Command class responsible for displaying detailed help information for each command.

    This class prints out all registered commands along with their descriptions.
    '''

    def __init__(self, command_handler):
        '''
        Constructor for HelpCommand, accepts a CommandHandler instance.

        Args:
        - command_handler (CommandHandler): The CommandHandler instance that manages command registration.
        '''
        self.command_handler = command_handler

    def execute(self):
        '''
        Executes the HelpCommand.

        This method prints the list of all commands with their descriptions.
        '''
        print("Help - Available Commands:\n")
        for command_name, command in self.command_handler.commands.items():
            description = command.__doc__.strip() if command.__doc__ else "No description available."
            print(f"{command_name}:\n\t{description}\n")

def register_commands(handler: CommandHandler):
    '''Registers the MenuCommand and HelpCommand with the command handler.'''
    handler.register_command('menu', MenuCommand(handler))
    handler.register_command('help', HelpCommand(handler))

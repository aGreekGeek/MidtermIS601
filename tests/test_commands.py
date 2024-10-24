'''Tests app/commands/__init__.py'''
from app.commands import Command, CommandHandler

class MockCommand(Command):
    '''A mock command class used for testing purposes.'''
    def execute(self):
        '''Mock implementation of the execute method.'''

def test_register_command():
    '''Verify that a command can be successfully registered.'''
    handler = CommandHandler()
    command = MockCommand()
    handler.register_command("test", command)
    assert "test" in handler.commands
    assert handler.commands["test"] == command

def test_execute_command():
    '''Check that a registered command is executed correctly.'''
    handler = CommandHandler()
    command = MockCommand()
    handler.register_command("test", command)
    handler.execute_command("test")

def test_execute_command_invalid(capfd):
    '''Ensure that trying to execute an invalid command prints the appropriate error message.'''
    handler = CommandHandler()

    # Attempt to execute a command that doesn't exist
    handler.execute_command("invalid_command")

    # Capture the output and confirm the error message is printed
    captured = capfd.readouterr()
    assert "No such command: invalid_command" in captured.out

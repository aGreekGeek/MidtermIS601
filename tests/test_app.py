'''Tests for app/__init__.py'''
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    '''Ensure the REPL terminates when 'exit' is entered.'''
    # Simulate user input for the 'exit' command
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()

    # Expect the REPL to raise a SystemExit when 'exit' is called
    with pytest.raises(SystemExit) as e:
        app.start()

    # Confirm the SystemExit exception is raised
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    '''Validate REPL's response to an unrecognized command.'''
    # Simulate user input: first an unknown command, then 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    # Expect SystemExit after the REPL processes commands
    with pytest.raises(SystemExit) as excinfo:  # pylint: disable=unused-variable
        app.start()

    # Optionally, verify a specific exit code if necessary
    # assert excinfo.value.code == expected_exit_code

    # Check that the unknown command was properly handled and the message displayed
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

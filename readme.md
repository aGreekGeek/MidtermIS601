# Advanced Python Calculator for Software Engineering Graduate Course
Developed by Steven Papadopoulos - IS601 Fall 2024

## Table of Contents
1. Project Overview
2. Features
3. Setup Instructions
4. Usage
5. Design Patterns
    - Facade Pattern
    - Command Pattern
    - Factory Method
    - Singleton Pattern
    - Strategy Pattern
6. Environment Variables
7. Logging Practices
8. Error Handling
9. Testing and Code Quality
10. Version Control
11. Video Demonstration

###  Project Overview

The Advanced Python Calculator is a command-line-based application designed to showcase professional software development practices. It provides fundamental arithmetic operations and manages calculation history using Pandas. This project integrates various design patterns, comprehensive logging, and dynamic configuration through environment variables. The application also includes a flexible plugin system for seamless integration of new features.

### Features

- Command-Line Interface (REPL) for direct user interaction.
- Arithmetic operations: Add, Subtract, Multiply, Divide.
- Advanced data handling using Pandas for calculation  history management.
- Dynamic plugin system to load and manage new features.
- Professional logging practices for better monitoring and debugging.
- Environment-based configuration for flexible setups.

### Setup Instructions

1.  Clone the Repository
2.  Create and Activate a Virtual Environment
3.  Install required Packages (See requirements.txt)
4.  Set up Environmental Variables if desired
5.  Run the Application (python3 main.py)

### Usage

1. Starting the Calculator:

    - Run the application and interact with the REPL by typing commands like add, subtract, history, etc.

2. Sample Commands:

    - Basic Operations: add, subtract, multiply, divide
    - History Management:
        - history to enter the submenu and manage records.
        - View, clear, save, load, sort, and filter calculation history.
    - Plugin Management: Dynamically loaded commands.

3. Video Demonstration:

Watch the Video Demo (below) for a walkthrough of key features.

### Design Patterns

1. Facade Pattern
    - Purpose
    The Facade pattern provides a simplified interface to a more complex system. In my application, the HistoryFacade class serves as a straightforward interface to interact with CalculationHistory. It hides the complexity of directly manipulating calculation data, making the code easier to use and maintain.

    - How it works
    The HistoryFacade class has methods like add_to_history, save_history, and load_history, which internally call methods from CalculationHistory. This way, other parts of the application don’t need to know how CalculationHistory works internally.

    - Code Exxample:

2. Command Pattern
    - Purpose
    The Command pattern encapsulates a request as an object, which allows you to parameterize methods, delay the execution of requests, or queue them. In my programs REPL, each command (e.g., AddCommand, SubtractCommand) implements the Command interface, making it easy to add or modify commands without affecting the core command-handling logic.

    - How it works
    Each command class (e.g., AddCommand) implements an execute method. The CommandHandler registers these commands and can dynamically execute them based on user input.

    - Code Example

3. Singleton Pattern
    - Purpose
    The Singleton pattern ensures that a class has only one instance throughout the program. This is useful for classes like CommandHandler that need to maintain a consistent state across multiple parts of the application.

    - How it works
    The CommandHandler is a Singleton, ensuring that only one instance is created and used throughout the application. This prevents issues with inconsistent command registration.

    - Code Example


4. Strategy Pattern
    - Purpose
    The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows algorithms to vary independently from the clients that use them. My application uses this pattern to handle different arithmetic operations

    - How it works
    Each arithmetic operation (addition, subtraction, etc.) is encapsulated in its own strategy class. The Calculator or Operations class can use these strategies interchangeably, which makes it easy to add or modify operations without altering existing code.

    - Code Example

### Environmental Variables
(.env included in .gitignore per professor instruction)
For logging my .env is configured with the following line of code:

export LOG_LEVEL=DEBUG
export LOG_FILE=logs/debug.log

Explanation:  Environment variables allow dynamic configuration of log levels, log files, and other settings, enabling flexible application behavior in different environments.

Usage: LOG_LEVEL: Controls the verbosity of logging (DEBUG, INFO, WARNING, ERROR).

### Logging Practices

- Explanation: The application uses a comprehensive logging system to record operations, errors, and other important events.
- Dynamic Configuration:  Log levels and destinations are controlled via environment variables.
- Pandas are utilized to handle and manage calculation history effectively to provides capabilities for loading, saving, sorting, and filtering history records, making data operations straightforward and efficient.
- Menu options exist to export calculation history to CSV files under history.

### Error Handling

1. Look Before You Leap (LBYL)
    - Example: The code is designed to check if the plugin directory exists before attempting to load plugins - if no plug in is found an error message will be provided

2.  Easier to Ask for Forgiveness than Permission (EAFP)
    - Example: Catching errors during arithmetic operations is integrated into the code for my program (i.e. controls for "division by 0")

### Testing and Code Quality

1. The application uses Pytest for comprehensive testing, ensuring over 90% test coverage. Tests cover arithmetic operations, command execution, and history management.

2. The application uses Pylint ot ensure adherance to PEP 8 standards

3. GitHub Actions are set up to run tests and code checks automatically on every push and pull request to my github repository, maintaining consistent code quality

### Video

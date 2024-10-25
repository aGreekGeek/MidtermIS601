from app.commands import Command
from app.calculator.calc_history import CalculationHistory as history

class HistoryMenuCommand(Command):
    '''Handles history-related submenu options in the REPL.'''

    def execute(self):
        '''
        Displays a submenu for managing calculation history.
        '''
        while True:
            print("\nHistory Menu:")
            print("1. View History")
            print("2. Clear History")
            print("3. Delete a Record")
            print("4. Back to Main Menu")
            
            choice = input("Select an option (1-4): ").strip()
            if choice == "1":
                self.view_history()
            elif choice == "2":
                self.clear_history()
            elif choice == "3":
                self.delete_history_record()
            elif choice == "4":
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def view_history(self):
        '''Displays the calculation history.'''
        history_list = history.get_history()
        if not history_list:
            print("No history available.")
        else:
            for i, calc in enumerate(history_list, 1):
                print(f"{i}. {calc}")

    def clear_history(self):
        '''Clears the entire calculation history.'''
        history.clear_history()
        print("History has been cleared.")

    def delete_history_record(self):
        '''Prompts the user to specify a record number to delete.'''
        record_num = input("Enter the record number to delete: ")
        try:
            index = int(record_num) - 1
            history_list = history.get_history()
            if index < 0 or index >= len(history_list):
                print("Invalid record number.")
            else:
                del history_list[index]
                print("Record deleted.")
        except ValueError:
            print("Please enter a valid number.")
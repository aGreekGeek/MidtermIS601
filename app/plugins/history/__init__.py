from app.commands import Command, CommandHandler
from app.calculator.calc_history import CalculationHistory as history

class HistoryMenuCommand(Command):
    '''Command class to handle the history submenu.'''

    def execute(self):
        '''
        Displays a submenu for managing calculation history operations.
        '''
        while True:
            print("\nHistory Menu:")
            print("1. View History")
            print("2. Clear History")
            print("3. Delete a Record")
            print("4. Save History to CSV")
            print("5. Load History from CSV")
            print("6. Sort History")
            print("7. Filter History")
            print("8. Back to Main Menu")

            choice = input("Select an option (1-8): ").strip()
            if choice == "1":
                self.view_history()
            elif choice == "2":
                self.clear_history()
            elif choice == "3":
                self.delete_history_record()
            elif choice == "4":
                self.save_history()
            elif choice == "5":
                self.load_history()
            elif choice == "6":
                self.sort_history()
            elif choice == "7":
                self.filter_history()
            elif choice == "8":
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def view_history(self):
        '''Displays the calculation history.'''
        print("Calculation History:")
        print(history.get_history())

    def clear_history(self):
        '''Clears the entire calculation history.'''
        history.clear_history()
        print("History has been cleared.")

    def delete_history_record(self):
        '''Prompts the user to specify a record number to delete.'''
        try:
            record_num = int(input("Enter the record number to delete: "))
            history.delete_record(record_num)
            print("Record deleted.")
        except ValueError:
            print("Please enter a valid number.")

    def save_history(self):
        '''Prompts for a filename and saves the history.'''
        filename = input("Enter the filename to save the history (default: calculation_history.csv): ") or "calculation_history.csv"
        history.save_history(filename)

    def load_history(self):
        '''Prompts for a filename and loads the history.'''
        filename = input("Enter the filename to load the history from (default: calculation_history.csv): ") or "calculation_history.csv"
        history.load_history(filename)

    def sort_history(self):
        '''Prompts the user to specify a column and sort order.'''
        column = input("Enter the column to sort by (Operand1, Operand2, Operation, Result): ").strip()
        order = input("Sort in ascending order? (yes/no): ").strip().lower()
        ascending = order == "yes"
        sorted_history = history.sort_history(by=column, ascending=ascending)
        print("Sorted Calculation History:")
        print(sorted_history)

    def filter_history(self):
        '''Prompts the user to specify an operation to filter by.'''
        operation = input("Enter the operation to filter by (addition, subtraction, multiplication, division): ").strip().lower()
        filtered_history = history.filter_history(operation)
        print(f"Filtered History (Operation: {operation}):")
        print(filtered_history)

def register_commands(handler: CommandHandler):
    '''Registers HistoryMenuCommand with the command handler.'''
    handler.register_command('history', HistoryMenuCommand())
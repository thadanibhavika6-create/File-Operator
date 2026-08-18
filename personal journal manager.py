import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"


    # 1. Add a New Entry
    def add_entry(self):

        try:
            entry = input("Enter your journal entry: ")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")


    # 2. View All Entries
    def view_entries(self):

        try:
            with open(self.filename, "r") as file:
                data = file.read()


            if data:
                print("\nYour Journal Entries:")
                print("--------------------------------")
                print(data)
            else:
                print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")


    # 3. Search for an Entry
    def search_entry(self):

        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                entries = file.read().split("\n\n")

            found = False

            print("\nMatching Entries:")
            print("--------------------------------")

            for entry in entries:

                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print("No entries were found for the keyword:", keyword)

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")


    # 4. Delete All Entries
    def delete_entries(self):

        try:

            confirm = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if confirm.lower() == "yes":

                os.remove(self.filename)

                print("All journal entries have been deleted.")

            elif confirm.lower() == "no":

                print("Deletion cancelled.")

            else:

                print("Invalid response. Please enter yes or no.")

        except FileNotFoundError:
            print("No journal entries to delete.")

        except PermissionError:
            print("Error: Permission denied. Cannot delete the file.")


    # Main Menu
    def menu(self):

        while True:

            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option:")
            print()
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            else:
                print("Invalid option. Please select a valid option from the menu.")


# Create Object
journal = JournalManager()

# Start Program
journal.menu()
from datetime import datetime
import os


class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("\nEnter your journal entry:\n> ").strip()

        if entry == "":
            print("Error: Journal entry cannot be empty.")
            return

        try:
            with open(self.filename, "x") as file:
                pass
        except FileExistsError:
            pass
        except PermissionError:
            print("Error: Permission denied.")
            return

        try:
            with open(self.filename, "a") as file:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                file.write(f"[{time}]\n")
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the file.")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if content.strip() == "":
                print("\nNo journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("-" * 40)
                print(content)

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied while reading the file.")

    def search_entry(self):
        keyword = input(
            "\nEnter a keyword or date to search:\n> "
        ).strip()

        if keyword == "":
            print("Error: Search keyword cannot be empty.")
            return

        try:
            with open(self.filename, "r") as file:
                content = file.read()

            entries = content.split("-" * 40)

            found = False

            print("\nMatching Entries:")
            print("-" * 40)

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry.strip())
                    print("-" * 40)
                    found = True

            if not found:
                print("No entries were found for:", keyword)

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied while reading the file.")

    def delete_entries(self):
        try:
            with open(self.filename, "r") as file:
                file.read()

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().lower()

            if confirmation != "yes":
                print("Deletion cancelled.")
                return

            with open(self.filename, "w") as file:
                file.write("")

            os.remove(self.filename)

            print("\nAll journal entries have been deleted.")

        except FileNotFoundError:
            print("\nNo journal entries to delete.")

        except PermissionError:
            print("\nError: Permission denied while deleting the file.")


def show_menu():
    print("\n" + "=" * 45)
    print("       PERSONAL JOURNAL MANAGER")
    print("=" * 45)
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    print("=" * 45)


def main():
    journal = JournalManager()

    print("\nWelcome to Personal Journal Manager!")

    while True:
        show_menu()

        choice = input("Please select an option (1-5): ").strip()

        if choice == "1":
            journal.add_entry()

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_entries()

        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid option.")
            print("Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
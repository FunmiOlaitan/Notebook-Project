from notebook import Notebook

class NotebookMenu:
    def __init__(self):
        self.notebook = Notebook()
    
    def display_menu(self):
        print("\\nNotebook Menu")
        print("1. New Note")
        print("2. Search Notes")
        print("3. Modify Note")
        print("4. Delete Note")
        print("5. Show All Notes")
        print("0. Exit")
    
    def run(self):
      while True:
        self.display_menu()
        choice = input("Enter your choice (0-5): ")

        if choice == "1":
            self.new_note()
        elif choice == "2":
            self.search_notes()
        elif choice == "3":
            self.modify_note()
        elif choice == "4":
            self.delete_note()
        elif choice == "5":
            self.show_all_notes()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

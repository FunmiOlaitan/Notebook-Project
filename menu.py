from notebook import Notebook

class NotebookMenu:
    def __init__(self):
        self.notebook = Notebook()
    
    def display_menu(self):
        """ Displaying the menu options:"""

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
    
    # Methods for menu options:
    def new_note(self):
        title = input("Enter note title: ")
        memo = input("Enter note memo")
        tags = input("Enter note tags(optional): ")
        self.notebook.new_note(title, memo, tags)
        print("Note added successfully")

    def search_notes(self):
        filter_str = input("Enter search filter: ")
        results = self.notebook.search(filter_str)
        if results:
            print("\\nSearch Results: ")
            for note in results:
                print("{0},\\n{1},\\n{2}\\n ".format(note.id, note.tags, note.memo))
        else:
            print("No matching notes found")
    
    def modify_note(self):
        note_id = int(input("Enter note ID to modify: "))
        title = input("Enter new title: ")
        memo = input("Enter a new memo: ")
        tags = input ("Enter a new tag: ")

        self.notebook.modify_title(note_id, title)
        self.notebook.modify_memo(note_id, memo)
        self.notebook.modify_tags(note_id, tags)
        print("Note modified successfully!")

    def delete_note(self):
        note_id = int(input("Enter note ID to delete: "))
        self.notebook.delete_note(note_id)
        print("Note deleted successfully!")
    
    def show_all_notes(self):
        self.notebook.show_notes()
    
if __name__ == "__main__":
    menu = NotebookMenu()
    menu.run()
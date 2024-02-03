import datetime

last_id = 0
class Note:

    """Represents a note with a title, memo, tags, creation date, and unique identifier."""
    def __init__(self,title, memo, tags=''):
        """Initializes a new Note instance with the provided title, memo, and optional tags."""
        self.title = title
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.now().date()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        """Checks if the note matches the given filter in its title, memo, or tags."""
        return filter in self.memo or filter in self.tags or filter in self.title
class Notebook:
    """Represents a collection of notes in a notebook."""
    
    def __init__(self):
        """Initializes a new Notebook instance with an empty list of notes."""
        self.notes = []

    def new_note(self, title, memo, tags=''):
        """Creates a new note and adds it to the notebook with the specified title, memo, and optional tags."""
        self.notes.append(Note(title, memo, tags))

    def _find_note(self, note_id):
      """Finds a note in the notebook based on its unique identifier. Returns None if not found."""
      for note in self.notes:
        if note.id == note_id:
            return note
      return None

    def modify_title(self, note_id, title):
      """Modifies the title of a note in the notebook identified by its unique identifier."""
      self._find_note(note_id).title = title

    def modify_memo(self, note_id, memo):
      """Modifies the memo of a note in the notebook identified by its unique identifier."""
      self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
      """Modifies the tags of a note in the notebook identified by its unique identifier."""
      self._find_note(note_id).tags = tags

    def search(self, filter):
        """Searches for notes in the notebook that match the given filter in titles, memos, or tags."""
        return [note for note in self.notes if note.match(filter)]
    
    def delete_note(self, note_id):
       """Deletes a note from the notebook based on its unique identifier."""
       self.notes = [note for note in self.notes if note.id != note_id]
    
    def show_notes(self, notes=None):
        """Displays the details of notes in the notebook. If notes is not provided, displays all notes."""
        if not notes:
            notes = self.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

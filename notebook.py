import datetime

last_id = 0
class Note:

    def __init__(self,title, memo, tags=''):
        self.title = title
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.creation_time = datetime.datetime.now()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        return filter in self.memo or filter in self.tags or filter in self.title
class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, title, memo, tags=''):
        self.notes.append(Note(title, memo, tags))

    def _find_note(self, note_id):
      for note in self.notes:
        if note.id == note_id:
            return note
        return None

    def modify_title(self, note_id, title):
      self._find_note(note_id).title = title

    def modify_memo(self, note_id, memo):
      self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
      self._find_note(note_id).tags = tags

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]
    
    def delete_note(self, note_id):
       self.notes = [note for note in self.notes if note.id != note_id]
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

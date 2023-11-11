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

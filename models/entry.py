class Entry():
    """Entry Class for return results of GET SQL query
    """
    def __init__(self, id, concept, entry, date, mood_id):
        self.id = id
        self.concept = concept
        self.entry = entry
        self.date = date
        self.mood_id = mood_id
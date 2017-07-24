from models.common import sort_array

class Event:
    events = []

    def __init__(self, date):
        '''date: Date object
        '''
        self.date = date

    def get_date(self):
        return self.date

    @classmethod
    def sort_events(cls):
        common.sort_array(cls.events)

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events

    def __gt__(self, other):
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

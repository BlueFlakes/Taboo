from models.common import sort_array
from datetime import datetime


class Event:
    events = []

    def __init__(self, event_topic, date):
        '''
        Args:
            date: Date object
            event_topic: str

        '''
        self.event_topic = event_topic.capitalize()
        self.date = date

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

    @classmethod
    def __str__(cls):
        for

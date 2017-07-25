from models.event import Event

class PublicEvent(Event):
    events = []

    def __init__(self, event_topic, date):
        super().__init__(event_topic, date)

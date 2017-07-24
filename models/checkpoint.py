from models.events import Event

class Checkpoint(Event):
    events = []

    def __init__(self, date):
        super().__init__(date)

        Event.add_event(self)
        Checkpoint.add_event(self)

    def __str__(self):
        return '{} Checkpoint'.format(self.date)

from models.event import Event

class Checkpoint(Event):
    events = []

    def __init__(self, date):
        super().__init__(date)
        Checkpoint.add_event(self)

    def __str__(self):
        return '{} Checkpoint'.format(self.date)

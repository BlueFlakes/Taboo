from models.events import Event

class PrivateMentoring(Event):
    events = []

    def __init__(self, date):
        super().__init__(date)
        self.preffered_mentor = None
        self.goal = None

        Event.add_event(self)
        self.__class__.add_event(self)

    def set_goal(self, goal):
        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):
        self.preffered_mentor = preffered_mentor

    def __str__(self):
        output_message = [self.date, self.preffered_mentor, self.goal]
        return '{} Private mentoring with {} about {}'.format(*output_message)

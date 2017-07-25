from models.event import Event
from data import tools
from datetime import datetime, timedelta

class PublicEvent(Event):
    events = []
    _file_name = 'csv/public_events.csv'

    def __init__(self, title, description, date):
        super().__init__(date)
        self.description = description.capitalize()
        self.title = title.title()

    @classmethod
    def load_public_events(cls):
        """Load public events from file"""
        cls.events = tools.get_data_from_file(cls._file_name, PublicEvent)

    @staticmethod
    def _prepare_public_events_data_to_save(existing_events):
        """Prepare PublicEvent objects to save

        Return:
            temp (list)

        """
        temp = []

        for event in existing_events:
            temp.append([event.title, event.description, str(event.date)])

        return temp

    @classmethod
    def save_public_events(cls):
        """save public events data to file"""
        prepared_data = cls._prepare_public_events_data_to_save(cls.events)
        tools.save_data_to_file(prepared_data, cls._file_name)


    @classmethod
    def prepare_events_data_to_visualize(cls):
        temp = []

        for event in cls.events:
            lighted_date = str(event.date)[:16]

            if event.date < (datetime.now() + timedelta(days=3)) and event.date > datetime.now():
                lighted_date = '\033[91m' + str(event.date)[:16] + '\033[0m'

            elif event.date < datetime.now():
                lighted_date = '\033[33m' + str(event.date)[:16] + '\033[0m'

            record = [lighted_date, event.title, event.description]
            temp.append(record)

        return temp

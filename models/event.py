from datetime import datetime, timedelta

class Event:
    events = []

    def __init__(self, date):
        '''
        Args:
            date: Date object
            event_topic: str

        '''
        date = self.get_expected_format_for_date(date)
        self.date = datetime.strptime(date, "%Y-%m-%d-%H-%M")


    @staticmethod
    def get_expected_format_for_date(record):
        if len(record) > 16:
            without_seconds = -3
            record = record.replace(' ', '-')
            record = record.replace(':', '-')
            record = record[:without_seconds]

        return record


    @classmethod
    def sort_events(cls):
        cls.sort_array(cls.events)


    @classmethod
    def delete_event(cls, idx):
        del cls.events[idx]

    @staticmethod
    def sort_array(array):

        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]

    @classmethod
    def get_number_of_events(cls):
        return len(cls.events)

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()


    @classmethod
    def archive_old_entries(cls):
        indexes_to_delete = cls._get_old_entries_indexes(cls.events)

        for index in indexes_to_delete[::-1]:
            del cls.events[index]


    @staticmethod
    def _get_old_entries_indexes(list_of_events):
        temp = []

        for i, event in enumerate(list_of_events):
            if event.date < datetime.now():
                temp.append(i)

        return temp


    @classmethod
    def get_events(cls):
        return cls.events

    def __gt__(self, other):
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

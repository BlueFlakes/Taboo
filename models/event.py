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
        """Check the length of record and then decide to modify it or not

        Args:
            record (str)

        Return:
            record (str)

        """
        if len(record) > 16:
            without_seconds = -3
            record = record.replace(' ', '-')
            record = record.replace(':', '-')
            record = record[:without_seconds]

        return record


    @classmethod
    def sort_events(cls):
        """Delegate sort events to responsible for this function"""
        cls.sort_array(cls.events)


    @classmethod
    def delete_event(cls, idx):
        """delete event from the list

        Args:
            idx (int)

        """
        del cls.events[idx]

    @staticmethod
    def sort_array(array):
        """Sort provided array in descending order

        Args:
            array (list)

        """
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]

    @classmethod
    def get_number_of_events(cls):
        """Returns the amount of existing events"""

        return len(cls.events)

    @classmethod
    def add_event(cls, event):
        """Add event to events list and then sort them

        Args:
            event (object)

        """
        cls.events.append(event)
        cls.sort_events()


    @classmethod
    def archive_old_entries(cls):
        """Archive out dated entries"""

        indexes_to_delete = cls._get_old_entries_indexes(cls.events)

        for index in indexes_to_delete[::-1]:
            del cls.events[index]


    @staticmethod
    def _get_old_entries_indexes(list_of_events):
        """Find and return indexes of entries which are out dated
        Args:
            list_of_events (list)

        Return:
            temp (list)

        """
        temp = []

        for i, event in enumerate(list_of_events):
            if event.date < datetime.now():
                temp.append(i)

        return temp


    @classmethod
    def get_events(cls):
        """return list of events"""
        return cls.events

    def __gt__(self, other):
        """Compare one object to another by date attribute"""
        return self.date > other.date

    def __lt__(self, other):
        """Compare one object to another by date attribute"""
        return self.date < other.date

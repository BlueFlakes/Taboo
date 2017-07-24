from datetime import date
from datetime import date, datetime
from data import tools


class RegistrationCode:
    registration_codes = []
    _file_name = 'csv/registration_codes.csv'

    def __init__(self, code, date):
        self.code = code
        self.date = datetime.strptime(date, "%Y-%m-%d").date()

    @classmethod
    def get_registration_codes(cls):
        return cls.registration_codes

    @classmethod
    def add_code(cls, code):
        """Add code to registration_codes

        Args:
            code (list)

        """
        cls.registration_codes.append(RegistrationCode(*code))

    @classmethod
    def find_code(cls, provided_code):
        """Check is provided_code in our registration_codes base

        Args:
            provided_code (str)

        Returns:
            used_code (RegistrationCode object)

        """
        used_code = None

        for i, regr_code in enumerate(cls.registration_codes):
            if provided_code == regr_code.code:
                used_code = cls.registration_codes.pop(i)
                break

        return used_code

    @classmethod
    def refresh_available_codes(cls):
        """Delete old registration codes from the database"""

        old_keys_indexes = cls.get_indexes_to_delete(cls.registration_codes)

        for index in old_keys_indexes[::-1]:
            del cls.registration_codes[index]

    @staticmethod
    def get_indexes_to_delete(registration_codes):
        """Find indexes which codes which are at least one day old.

        Args:
            registration_codes (list)

        Returns:
            temp (list)

        """

        current_date = date.today()
        temp = []

        for i, code in enumerate(registration_codes):
            if code.date != current_date:
                temp.append(i)

        return temp

    @classmethod
    def load_registration_codes(cls):
        """Load registration codes from file"""
        cls.registration_codes = tools.get_data_from_file(cls._file_name, RegistrationCode)

    @staticmethod
    def _prepare_registration_codes_data_to_save(registration_codes):
        """Prepare RegistrationCode objects to save

        Return:
            temp (list)

        """
        temp = []

        for regr_code in registration_codes:
            temp.append([regr_code.code, str(regr_code.date)])

        return temp

    @classmethod
    def save_registration_codes(cls):
        """save registration codes data to file"""
        prepared_data = cls._prepare_registration_codes_data_to_save(cls.registration_codes)
        tools.save_data_to_file(prepared_data, cls._file_name)



#

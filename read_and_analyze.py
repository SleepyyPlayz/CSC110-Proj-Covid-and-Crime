import csv
import datetime


class EmergencyCall:
    """A data type representing the specific 911 call.

    This corresponds to one row of the data in police_data.csv with the irrelevant columns removed

    Attributes:
        - date: the date of the call
        - emergency: the reason for the call
        - location: the location of the incident

    Representation Invariants:
        - pass
    """
    date: datetime.date
    emergency: str
    location: str

    def __init__(self, date: datetime.date, emergency: str, location: str) -> None:
        self.date = date
        self.emergency = emergency
        self.location = location


def read_covid_data(filename: str) -> list[list]:
    """Return the data table stored in the covid_data csv file with the given filename.
    The return value is a list of lists. The nested lists represent each row of necessary
    information.
    Preconditions:
      - filename refers to a valid csv file with headers
    """
    # "open" is a builtin function that accesses a file on your computer,
    # looking in the same folder as the current Python module.
    # "with" is a special type of compound statement in Python that
    # works with "open" to create a new variable "file" that you can use
    # inside the with block to access the file.
    with open(filename) as file:
        # This line creates a csv reader, which is a Python value that
        # can read csv data from a given file (essentially splitting up the
        # file into rows, and splitting each row by commas).
        reader = csv.reader(file)

        # This line reads the first row of the csv file, which contains the headers.
        # The result is a list of strings.
        headers = next(reader)

        # This list comprehension reads each remaining row of the file,
        # where each row is represented as a list of strings.
        # The header row is *not* included in this list.

        # comprehension converts rows into correct data type
        # data = [ for row in reader]


def read_police_data(filename: str) -> list[list]:
    """Return the data table stored in the police_data csv file with the given filename.
    The return value is a list of lists. The nested lists represent each row of necessary
    information.
    Preconditions:
      - filename refers to a valid csv file with headers
    """
    # "open" is a builtin function that accesses a file on your computer,
    # looking in the same folder as the current Python module.
    # "with" is a special type of compound statement in Python that
    # works with "open" to create a new variable "file" that you can use
    # inside the with block to access the file.
    with open(filename) as file:
        # This line creates a csv reader, which is a Python value that
        # can read csv data from a given file (essentially splitting up the
        # file into rows, and splitting each row by commas).
        reader = csv.reader(file)

        # This line reads the first row of the csv file, which contains the headers.
        # The result is a list of strings.
        headers = next(reader)

        # This list comprehension reads each remaining row of the file,
        # where each row is represented as a list of strings.
        # The header row is *not* included in this list.

        # comprehension converts rows into correct data type
        # data = [ for row in reader]


def covid_data_str_to_date(date_str: str) -> datetime.date:
    """Convert a string in the yyyy-mm-dd format to a datetime.date

    Preconditions:
        - len(date_str) == 10
        - date_str[4] == '-'
        - date_str[7] == '-'
        - int(date_str[:4]) >= 0
        - 0 <= int(date_str[5:7]) <= 12
        - 0 <= int(date_str[8:]) <= 31

    >>> covid_data_str_to_date('2020-01-01')
    datetime.date(2020, 1, 1)
    >>> covid_data_str_to_date('1999-12-31')
    datetime.date(1999, 12, 31)
    """


def police_data_str_to_date(date_str: str) -> datetime.date:
    """Convert a string in the yyyy-mm format to a datetime.date with the day
    being the last day of the corresponding month.

    Preconditions:
        - len(date_str) == 7
        - date_str[4] == '-'
        - int(date_str[:4]) >= 0
        - 0 <= int(date_str[5:]) <= 12

    >>> covid_data_str_to_date('2020-01')
    datetime.date(2020, 1, 31)
    >>> covid_data_str_to_date('1999-12')
    datetime.date(1999, 2, 28)
    """


def filter_physical_crimes(data: list[list]) -> list[list]:
    """Remove the row entries in data that do not correspond to physical crimes

    Preconditions:
        - len(data) != 0
    """

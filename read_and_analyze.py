import csv
import datetime

PROV_AND_TERR = {'British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec',
                 'Newfoundland & Labrador', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
                 'Northwest Territories', 'Nunavut', 'Yukon'}

DAYS_PER_MONTH = {1: 31,
                  2: 28,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31}


class EmergencyCall:
    """A data type representing the specific 911 call.

    Each instance corresponds to one row of data in police_data.csv with the irrelevant columns removed

    Attributes:
      - date: the date of the call
      - emergency: the reason for the call
      - location: the location of the incident

    Representation Invariants:
      - self.emergency != ''
      - self.location != ''
    """
    date: datetime.date
    emergency: str
    location: str

    def __init__(self, date: datetime.date, emergency: str, location: str) -> None:
        self.date = date
        self.emergency = emergency
        self.location = location


class CovidData:
    """A data type representing the covid data for the day.

    Each instance corresponds to one row of data in covid_data.csv

    Attributes:
        - date: the date of the data
        - num_confirmed: the number of new confirmed cases on date for prov_terr
        - num_deaths: the number of new covid related deaths on date for prov_terr
        - num_active: the total number of active cases for prov_terr as of date
        - prov_terr: the province or territory that corresponds with the covid data

    Representation Invaraints:
      - self.num_confirmed >= 0
      - self.num_deaths >= 0
      - self.num_active >= 0
      - self.prov_terr in PROV_AND_TERR
    """
    prov_terr: str
    date: datetime.date
    num_active: int
    num_deaths: int

    def __init__(self, prov_terr: str, date: datetime.date, num_active: int, num_deaths: int) -> None:
        self.prov_terr = prov_terr
        self.date = date
        self.num_active = num_active
        self.num_deaths = num_deaths


def read_covid_data(filename: str) -> list[CovidData]:
    """Return the data table stored in the covid_data csv file with the given filename.
    The return value is a list of lists. The nested lists represent each row of necessary
    information.
    Preconditions:
      - filename refers to a valid csv file with headers
    """
    with open(filename) as file:
        reader = csv.reader(file)

        headers = next(reader)

        return [CovidData(row[1], covid_data_str_to_date(row[3]), int(row[5]), int(row[7])) for row in reader]


def read_police_data(filename: str) -> list[EmergencyCall]:
    """Return the data table stored in the police_data csv file with the given filename.
    The return value is a list of EmergencyCall. Each EmergencyCall instance is a row of information.
    Preconditions:
      - filename refers to a valid csv file with headers
    """
    with open(filename) as file:
        reader = csv.reader(file)

        headers = next(reader)




def covid_data_str_to_date(date_str: str) -> datetime.date:
    """Convert a string in the yyyy-mm-dd format (from the covid_data.csv file) to a datetime.date

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
    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:])

    return datetime.date(year, month, day)


def police_data_str_to_date(date_str: str) -> datetime.date:
    """Convert a string in the yyyy-mm format (from the police_data.csv file) to a datetime.date with the day
    being the last day of the corresponding month.

    Preconditions:
      - len(date_str) == 7
      - date_str[4] == '-'
      - int(date_str[:4]) >= 0
      - 0 <= int(date_str[5:]) <= 12

    >>> covid_data_str_to_date('2020-01')
    datetime.date(2020, 1, 31)
    >>> covid_data_str_to_date('1999-02')
    datetime.date(1999, 2, 28)
    """
    year = int(date_str[:4])
    month = int(date_str[5:7])
    if month == 2 and year % 4 == 0:
        day = 29
    else:
        day = DAYS_PER_MONTH[month]

    return datetime.date(year, month, day)


def filter_physical_crimes(data: list[EmergencyCall]) -> list[EmergencyCall]:
    """Return a new list of EmergencyCall with only physical crimes.

    Preconditions:
      - len(data) != 0

    >>> call1 = EmergencyCall(datetime.date(2020, 1, 31), 'assault', 'Fake Street E')
    >>> call2 = EmergencyCall(datetime.date(2020, 2, 29), 'suicide', 'Fake Street W')
    >>> filter_physical_crimes([call1, call2])
    [call1]
    """


def filter_by_covid_case_per_month(data: list[CovidData], prov_terr: str, month: int, year: int) -> list[CovidData]:
    """Return a new list of CovidData with only CovidData corresponding to month, year for prov_terr

    Preconditions:
      - len(data) != 0
      - year >= 0
      - 1 <= month <= 12
      - prov_terr in PROV_AND_TERR
    """


def calc_covid_case_per_month(data: list[CovidData], prov_terr: str, month: int, year: int) -> tuple[int, int]:
    """Return a tuple of the total number of new confirmed covid cases in month, year, represented as an int,
    for the given prov_terr and the total number of new covid related deaths in month, represented as an int, for the
    given prov_terr

    Preconditions:
      - len(data) != 0
      - year >= 0
      - 1 <= month <= 12
      - prov_terr in PROV_AND_TERR
    """

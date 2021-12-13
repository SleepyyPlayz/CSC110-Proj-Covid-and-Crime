"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""
import csv
import datetime

PROV_AND_TERR = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec',
                 'Newfoundland and Labrador', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
                 'Northwest Territories', 'Nunavut', 'Yukon']

PROV_AND_TERR_KEYWORDS = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec',
                          'Newfoundland', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
                          'Northwest Territories', 'Nunavut', 'Yukon']

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
    """A data type representing the specific 911 call. Each instance corresponds to one row of data in police_data.csv
    with the irrelevant columns removed.

    Attributes:
      - date: the date of the call
      - _emergency: the reason for the call
      - _location: the location of the incident (either a province, territory, or just Canada)
      - _num_incidents: the number of calls for emergency in the month of date

    Representation Invariants:
      - self._emergency != ''
      - self._location in PROV_AND_TERR or self._location == "Canada"
    """
    date: datetime.date
    _location: str
    _emergency: str
    _num_incidents: int

    def __init__(self, date: datetime.date, location: str, emergency: str, num_incidents: int) -> None:
        """Initialize a new EmergencyCall instance"""
        self.date = date
        self._location = location
        self._emergency = emergency
        self._num_incidents = num_incidents

    def get_location(self) -> str:
        """Return the location of the EmergencyCall instance"""
        return self._location

    def get_emergency(self) -> str:
        """Return the emergency of the EmergencyCall instance"""
        return self._emergency

    def get_num_incidents(self) -> int:
        """Return the number of calls for a certain emergency in the month corresponding to date"""
        return self._num_incidents


class CovidData:
    """A data type representing the covid data for the day. Each instance corresponds to one row of data in
    covid_data.csv.

    Attributes:
      - date: the date of the data
      - _location: the location that corresponds with the covid data (either a province, territory, or just Canada)
      - _num_active: the total number of active cases for prov_terr as of date
      - _num_deaths: the total number of COVID related deaths on date for prov_terr

    Representation Invariants:
      - self._num_deaths >= 0
      - self._num_active >= 0
      - self._location in PROV_AND_TERR or self._location == "Canada"
    """
    date: datetime.date
    _location: str
    _num_active: int
    _num_deaths: int

    def __init__(self, date: datetime.date, location: str, num_active: int, num_deaths: int) -> None:
        """Initialize a new covid data instance"""
        self.date = date
        self._location = location
        self._num_active = num_active
        self._num_deaths = num_deaths

    def get_location(self) -> str:
        """Return the location that corresponds with CovidData"""
        return self._location

    def get_num_active(self) -> int:
        """Return the number of active cases that corresponds with the instance of CovidData"""
        return self._num_active

    def get_num_deaths(self) -> int:
        """Return the number of COVID related deaths that corresponds with the instance of CovidData"""
        return self._num_deaths


def read_covid_data(filename: str) -> list[CovidData]:
    """Return the data table stored in the covid_data csv file with the given filename.
    The return value is a list of CovidData. Each CovidData instance is a row of information.

    Preconditions:
      - filename refers to a valid csv file with headers
    """
    covid_data_so_far = []

    with open(filename) as file:
        reader = csv.reader(file)

        _ = next(reader)

        for row in reader:
            if row[1] in PROV_AND_TERR or row[1] == "Canada":
                covid_data_so_far.append(CovidData(covid_data_str_to_date(row[3]), row[1], int(row[5]), int(row[7])))

    return covid_data_so_far


def read_police_data(filename: str) -> list[EmergencyCall]:
    """Return the data table stored in the police_data csv file with the given filename. The return value is a list of
    EmergencyCall. Each EmergencyCall instance is a row of information.

    Preconditions:
      - filename refers to a valid csv file with headers
    """
    police_data_so_far = []

    with open(filename) as file:
        reader = csv.reader(file)

        _ = next(reader)

        for row in reader:
            date = police_data_str_to_date(row[0])
            if "Royal Canadian Mounted Police" not in row[1]:
                location = det_location(row[1])
            else:
                continue

            if row[11] == '':
                incidences = 0
            else:
                incidences = int(row[11])

            emergency_call = EmergencyCall(date, location, row[3], incidences)
            police_data_so_far.append(emergency_call)

        return police_data_so_far


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

    >>> police_data_str_to_date('2020-01')
    datetime.date(2020, 1, 31)
    >>> police_data_str_to_date('1999-02')
    datetime.date(1999, 2, 28)
    """
    year = int(date_str[:4])
    month = int(date_str[5:7])
    if month == 2 and year % 4 == 0:
        day = 29
    else:
        day = DAYS_PER_MONTH[month]

    return datetime.date(year, month, day)


def det_location(location: str) -> str:
    """Return the province or territory based on location and Canada if it cannot be determined

    Preconditions:
      - len(location) != 0

    >>> det_location("Royal Newfoundland Constabulary")
    'Newfoundland and Labrador'
    >>> det_location("Total, Selected police services")
    'Canada'
    """
    for i in range(len(PROV_AND_TERR_KEYWORDS)):
        if PROV_AND_TERR_KEYWORDS[i] in location:
            return PROV_AND_TERR[i]

    return "Canada"


def get_crimes_only() -> set[str]:
    """Return a set containing unique crimes in dataset"""
    crimes = set()
    emergency_calls = read_police_data('data_sets/police_data.csv')

    for call in emergency_calls:
        crimes.add(call.get_emergency())

    return crimes


def get_locations_only(filename: str) -> set[str]:
    """Return a set containing unique locations in dataset"""
    locations = set()

    with open(filename) as file:
        reader = csv.reader(file)

        _ = next(reader)

        for row in reader:
            locations.add(row[1])

    return locations


# if __name__ == '__main__':
#     import python_ta
#     import python_ta.contracts
#
#     python_ta.contracts.DEBUG_CONTRACTS = False
#     python_ta.contracts.check_all_contracts()
#
#     python_ta.check_all(config={
#         'extra-imports': ['datetime', 'csv'],  # the names (strs) of imported modules
#         'allowed-io': ['read_covid_data', 'read_police_data'],  # the names (strs) of functions that call
#                                                                 # print/open/input
#         'max-line-length': 120,
#         'disable': ['R1705', 'C0200']
#     })

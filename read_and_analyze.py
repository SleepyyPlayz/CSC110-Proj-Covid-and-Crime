import csv
import datetime

PROV_AND_TERR = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec',
                 'Newfoundland and Labrador', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
                 'Northwest Territories', 'Nunavut', 'Yukon']

PROV_AND_TERR_KEYWORDS = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec',
                          'Newfoundland', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
                          'Northwest Territories', 'Nunavut', 'Yukon']

CRIMES = {'assault', 'breaking and entering', 'domestic disturbance', 'dangerous operation', 'death', 'harm',
          'robbery', 'comply with order', 'fraud', 'impaired driving', 'theft', 'shoplifting'}

PHYSICAL_CRIMES = {'assault', 'domestic disturbance', 'dangerous operation', 'death', 'harm', 'robbery'}

PUBLIC = {'public', 'non-family', 'unknown', 'non-residential', 'mental health act', 'dangerous operation',
          'comply with order', 'impaired driving', 'theft', 'provincial/territorial', 'shoplifting',
          'robbery'}

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
      - _num_deaths: the number of new covid related deaths on date for prov_terr

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
        """Return the number of new covid related deaths that corresponds with the instance of CovidData"""
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
            location = det_location(row[1])
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


def filter_just_crimes(data: list[EmergencyCall]) -> list[EmergencyCall]:
    """Returns list of EmergencyCall instances that are crimes, with other types of emergencies omitted

    Preconditions:
      - len(data) != 0

    >>> call1 = EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = EmergencyCall(datetime.date(2020, 2, 29), 'Ontario', \
    'Calls for service, suicide/attempted suicide', 16)
    >>> filter_just_crimes([call1, call2]) == [call1]
    True
    """
    crimes = []

    for call in data:
        for crime in CRIMES:
            if crime in call.get_emergency().lower():
                crimes.append(call)
                break

    return crimes


def filter_crimes_by_type(data: list[EmergencyCall], filter_type: str) -> \
        tuple[list[EmergencyCall], list[EmergencyCall]]:
    """Return tuple that contains lists of EmergencyCall instances, one selecting for the filter_type
    and one against the filter_type.

    Preconditions:
      - data contains only crimes, with other types of emergencies omitted
      - len(data) != 0
      - filter_type == 'public' or filter_type == 'physical'

    >>> call1 = EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = EmergencyCall(datetime.date(2020, 2, 29), 'Ontario', \
    'Calls for service, suicide/attempted suicide', 16)
    >>> filter_crimes_by_type([call1, call2], 'physical')[0] == [call1]
    True
    >>> filter_crimes_by_type([call1, call2], 'public')[0] == [call1]
    True
    """
    filter_included = []
    filter_excluded = []
    if filter_type == 'public':
        keywords = PUBLIC
    else:
        keywords = PHYSICAL_CRIMES

    for call in data:
        include = False
        for crime in keywords:
            if crime in call.get_emergency().lower():
                include = True
                break

        if include:
            filter_included.append(call)
        else:
            filter_excluded.append(call)

    return filter_included, filter_excluded


def filter_data_by_month(data: list, location: str, month: int, year: int) -> list:
    """Return a new list of data with only data corresponding to month, year for location

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == "Canada"
      - 1 <= month <= 12
      - year >= 0

    >>> call1 = EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Calls for service, suicide/attempted suicide', 16)
    >>> filter_data_by_month([call1, call2], 'Ontario', 1, 2020) == [call1, call2]
    True
    >>> covid_data1 = CovidData(datetime.date(2020, 1, 1), 'Ontario', 1, 1)
    >>> covid_data2 = CovidData(datetime.date(2021, 1, 2), 'Ontario', 1, 1)
    >>> covid_data3 = CovidData(datetime.date(2020, 1, 3), 'Quebec', 1, 1)
    >>> filter_data_by_month([covid_data1, covid_data2, covid_data3], 'Ontario', 1, 2020) == [covid_data1]
    True
    """
    filtered_so_far = []

    for info in data:
        if info.date.month == month and info.date.year == year and info.get_location() == location:
            filtered_so_far.append(info)

    return filtered_so_far


def get_crimes_only() -> set[str]:
    """Return a set containing unique crimes in dataset"""
    crimes = set()
    emergency_calls = read_police_data('data_sets/police_data.csv')

    for call in emergency_calls:
        crimes.add(call.get_emergency())

    return crimes

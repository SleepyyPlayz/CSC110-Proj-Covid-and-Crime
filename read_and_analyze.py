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


def filter_crimes_by_location(data: list[EmergencyCall], location: str, year: int) -> list[EmergencyCall]:
    """Return a new list of EmergencyCall with only data corresponding to year for location

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == "Canada"
      - year >= 0

    >>> call1 = EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Calls for service, suicide/attempted suicide', 16)
    >>> filter_crimes_by_location([call1, call2], 'Ontario', 2020) == [call1, call2]
    True
    """
    filtered_so_far = []

    for call in data:
        if call.date.year == year and call.get_location() == location:
            filtered_so_far.append(call)

    return filtered_so_far


def get_monthly_cases(data: list[CovidData], year: int, location: str) -> list[CovidData]:
    """Return a list of CovidData with only the data for the last day of each month for a particular year for a
    particular location

    Preconditions:
      - len(data) != 0
      - year >= 0
      - location in PROV_AND_TERR or location == 'Canada'

    >>> covid_data1 = CovidData(datetime.date(2020, 1, 31), 'Ontario', 1, 1)
    >>> covid_data2 = CovidData(datetime.date(2020, 2, 29), 'Ontario', 1, 1)
    >>> covid_data3 = CovidData(datetime.date(2020, 1, 29), 'Ontario', 1, 1)
    >>> covid_data4 = CovidData(datetime.date(2021, 1, 31), 'Ontario', 1, 1)
    >>> covid_data5 = CovidData(datetime.date(2020, 1, 31), 'Quebec', 1, 1)
    >>> data = [covid_data1, covid_data2, covid_data3, covid_data4, covid_data5]
    >>> get_monthly_cases(data, 2020, 'Ontario') == [covid_data1, covid_data2]
    True
    """
    covid_data_so_far = []

    for covid_data in data:
        if covid_data.date.year == year and covid_data.get_location() == location and check_if_monthly_case(covid_data):
            covid_data_so_far.append(covid_data)

    return covid_data_so_far


def check_if_monthly_case(covid_data: CovidData) -> bool:
    """Return whether the CovidData instance is data for the last day of a certain month in a certain year for a
    particular location

    >>> covid_data1 = CovidData(datetime.date(2020, 1, 31), 'Ontario', 1, 1)
    >>> check_if_monthly_case(covid_data1)
    True
    >>> covid_data2 = CovidData(datetime.date(2020, 1, 30), 'Ontario', 1, 1)
    >>> check_if_monthly_case(covid_data2)
    False
    """
    if covid_data.date.month == 2 and covid_data.date.day == 29:
        return True

    for month in DAYS_PER_MONTH:
        if covid_data.date.month == month and covid_data.date.day == DAYS_PER_MONTH[month]:
            return True

    return False


def covid_data_to_dict(data: list[CovidData]) -> dict[str: list]:
    """Return a dictionary mapping the attributes of CovidData to a list of attributes for all the CovidData instances
    in data

    Preconditions:
      - len(data) != 0

    >>> covid_data1 = CovidData(datetime.date(2020, 1, 1), 'Ontario', 1, 1)
    >>> expected = {'Date': [datetime.date(2020, 1, 1)], 'Number of Active Cases': [1], \
    'Number of Deaths': [1]}
    >>> covid_data_to_dict([covid_data1]) == expected
    True
    """
    dict_so_far = {'Date': [], 'Number of Active Cases': [], 'Number of Deaths': []}

    for covid_data in data:
        dict_so_far['Date'].append(covid_data.date)
        dict_so_far['Number of Active Cases'].append(covid_data.get_num_active())
        dict_so_far['Number of Deaths'].append(covid_data.get_num_deaths())

    return dict_so_far


def emergency_call_to_dict(data: list[EmergencyCall]) -> dict[str, list]:
    """Return a dictionary mapping the attributes of EmergencyCall to a list of attributes for all the EmergencyCall
     instances in data

    Preconditions:
      - len(data) != 0

    >>> from pprint import pprint
    >>> call1 = EmergencyCall(datetime.date(2020, 1, 1), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 1)
    >>> expected = {'Date': [datetime.date(2020, 1, 1)], \
    'Emergency': ['Impaired driving, causing death or bodily harm [921]'], 'Number of Incidents': [1]}
    >>> emergency_call_to_dict([call1]) == expected
    True
    """
    dict_so_far = {'Date': [], 'Emergency': [], 'Number of Incidents': []}

    for call in data:
        dict_so_far['Date'].append(call.date)
        dict_so_far['Emergency'].append(call.get_emergency())
        dict_so_far['Number of Incidents'].append(call.get_num_incidents())

    return dict_so_far


def get_police_data(data: list[EmergencyCall], location: str, year: int, category: str) -> \
        tuple[dict[str, list], dict[str, list]]:
    """Return a tuple of 2 dictionaries. The first dictionary contains the yearly crime, in a particular
    category, for location during year. The second dictionary contains the yearly crime, in the opposite of the
    category, for location during year.

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == 'Canada'
      - year >= 0
      - category == 'public' or category == 'physical'
    """
    crimes = filter_just_crimes(data)
    crimes_in_location = filter_crimes_by_location(crimes, location, year)
    crimes_category, crimes_opp_category = filter_crimes_by_type(crimes_in_location, category)
    category_dict = emergency_call_to_dict(crimes_category)
    opp_category_dict = emergency_call_to_dict(crimes_opp_category)

    return category_dict, opp_category_dict


def get_police_data_totals(data: list[EmergencyCall], location: str, year: int, category: str) -> \
        tuple[dict[str, list], dict[str, list]]:
    """Return a tuple of 2 dictionaries. The first dictionary contains the total crime in a specific category, at a
    location during year. The second dictionary contains the total crime in the opposite of the
    category, at a location during year.

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == 'Canada'
      - year >= 0
      - category == 'public' or category == 'physical'
    """
    total_cat_dict_so_far = {'Date': [], 'Emergency': [], 'Number of Incidents': []}
    total_opp_cat_dict_so_far = {'Date': [], 'Emergency': [], 'Number of Incidents': []}

    category_dict, opp_category_dict = get_police_data(data, location, year, category)

    for i in range(len(category_dict['Date'])):
        if 'Total' in category_dict['Emergency']:
            total_cat_dict_so_far['Date'].append(category_dict['Date'][i])
            total_cat_dict_so_far['Emergency'].append(category_dict['Emergency'][i])
            total_cat_dict_so_far['Number of Incidents'].append(category_dict['Number of Incidents'][i])

    for i in range(len(opp_category_dict['Date'])):
        if 'Total' in opp_category_dict['Emergency']:
            total_opp_cat_dict_so_far['Date'].append(category_dict['Date'][i])
            total_opp_cat_dict_so_far['Emergency'].append(category_dict['Emergency'][i])
            total_opp_cat_dict_so_far['Number of Incidents'].append(category_dict['Number of Incidents'][i])

    return total_cat_dict_so_far, total_opp_cat_dict_so_far


def get_covid_data(data: list[CovidData], location: str, year: int) -> dict[str, list]:
    """Return a dictionary of the covid data on the last day of each month for a specific year at a specific location

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == 'Canada'
      - year >= 0
    """
    covid_in_location = get_monthly_cases(data, year, location)

    return covid_data_to_dict(covid_in_location)


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

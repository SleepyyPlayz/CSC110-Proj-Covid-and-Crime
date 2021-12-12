"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""
import read

CRIMES = {'assault', 'breaking and entering', 'domestic disturbance', 'dangerous operation', 'death', 'harm',
          'robbery', 'comply with order', 'fraud', 'impaired driving', 'theft', 'shoplifting'}

PHYSICAL_CRIMES = {'assault', 'domestic disturbance', 'dangerous operation', 'death', 'harm', 'robbery'}

PUBLIC = {'public', 'non-family', 'unknown', 'non-residential', 'mental health act', 'dangerous operation',
          'comply with order', 'impaired driving', 'theft', 'provincial/territorial', 'shoplifting',
          'robbery'}


def filter_just_crimes(data: list[read.EmergencyCall]) -> list[read.EmergencyCall]:
    """Returns list of EmergencyCall instances that are crimes, with other types of emergencies omitted

    Preconditions:
      - len(data) != 0

    >>> import datetime
    >>> call1 = read.EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = read.EmergencyCall(datetime.date(2020, 2, 29), 'Ontario', \
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


def filter_crimes_by_type(data: list[read.EmergencyCall], filter_type: str) -> \
        tuple[list[read.EmergencyCall], list[read.EmergencyCall]]:
    """Return tuple that contains lists of EmergencyCall instances, one selecting for the filter_type
    and one against the filter_type.

    Preconditions:
      - data contains only crimes, with other types of emergencies omitted
      - len(data) != 0
      - filter_type == 'public' or filter_type == 'physical'

    >>> import datetime
    >>> call1 = read.EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = read.EmergencyCall(datetime.date(2020, 2, 29), 'Ontario', \
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


def filter_crimes_by_location(data: list[read.EmergencyCall], location: str, year: int) -> list[read.EmergencyCall]:
    """Return a new list of EmergencyCall with only data corresponding to year for location

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == "Canada"
      - year >= 0

    >>> import datetime
    >>> call1 = read.EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Impaired driving, causing death or bodily harm [921]', 34)
    >>> call2 = read.EmergencyCall(datetime.date(2020, 1, 31), 'Ontario', \
    'Calls for service, suicide/attempted suicide', 16)
    >>> filter_crimes_by_location([call1, call2], 'Ontario', 2020) == [call1, call2]
    True
    """
    filtered_so_far = []

    for call in data:
        if call.date.year == year and call.get_location() == location:
            filtered_so_far.append(call)

    return filtered_so_far


def get_monthly_cases(data: list[read.CovidData], year: int, location: str) -> list[read.CovidData]:
    """Return a list of CovidData with only the data for the last day of each month for a particular year for a
    particular location

    Preconditions:
      - len(data) != 0
      - year >= 0
      - location in PROV_AND_TERR or location == 'Canada'

    >>> import datetime
    >>> covid_data1 = read.CovidData(datetime.date(2020, 1, 31), 'Ontario', 1, 1)
    >>> covid_data2 = read.CovidData(datetime.date(2020, 2, 29), 'Ontario', 1, 1)
    >>> covid_data3 = read.CovidData(datetime.date(2020, 1, 29), 'Ontario', 1, 1)
    >>> covid_data4 = read.CovidData(datetime.date(2021, 1, 31), 'Ontario', 1, 1)
    >>> covid_data5 = read.CovidData(datetime.date(2020, 1, 31), 'Quebec', 1, 1)
    >>> data = [covid_data1, covid_data2, covid_data3, covid_data4, covid_data5]
    >>> get_monthly_cases(data, 2020, 'Ontario') == [covid_data1, covid_data2]
    True
    """
    covid_data_so_far = []

    for covid_data in data:
        if covid_data.date.year == year and covid_data.get_location() == location and check_if_monthly_case(covid_data):
            covid_data_so_far.append(covid_data)

    return covid_data_so_far


def check_if_monthly_case(covid_data: read.CovidData) -> bool:
    """Return whether the CovidData instance is data for the last day of any month.

    >>> import datetime
    >>> covid_data1 = read.CovidData(datetime.date(2020, 1, 31), 'Ontario', 1, 1)
    >>> check_if_monthly_case(covid_data1)
    True
    >>> covid_data2 = read.CovidData(datetime.date(2020, 1, 30), 'Ontario', 1, 1)
    >>> check_if_monthly_case(covid_data2)
    False
    """
    if covid_data.date.month == 2 and covid_data.date.day == 29:
        return True

    for month in read.DAYS_PER_MONTH:
        if covid_data.date.month == month and covid_data.date.day == read.DAYS_PER_MONTH[month]:
            return True

    return False


def covid_data_to_dict(data: list[read.CovidData]) -> dict[str: list]:
    """Return a dictionary mapping relevant attributes of CovidData to a list of attributes for all the CovidData
    instances in data

    Preconditions:
      - len(data) != 0

    >>> import datetime
    >>> covid_data1 = read.CovidData(datetime.date(2020, 1, 1), 'Ontario', 1, 1)
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


def emergency_call_to_dict(data: list[read.EmergencyCall]) -> dict[str, list]:
    """Return a dictionary mapping the relevant attributes of EmergencyCall to a list of attributes for all the
    EmergencyCall instances in data

    Preconditions:
      - len(data) != 0

    >>> import datetime
    >>> call1 = read.EmergencyCall(datetime.date(2020, 1, 1), 'Ontario', \
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


def get_police_data(data: list[read.EmergencyCall], location: str, year: int, category: str) -> \
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


def get_police_data_totals(data_dict: dict[str, list]) -> dict[str, list]:
    """Return a new dictionary with the same keys. For the values, only append the data that track the total crimes

    Preconditions:
      - len(data_dict) != 0
    """
    total_dict_so_far = {'Date': [], 'Emergency': [], 'Number of Incidents': []}

    for i in range(len(data_dict['Date'])):
        if 'Total' in data_dict['Emergency'][i]:
            total_dict_so_far['Date'].append(data_dict['Date'][i])
            total_dict_so_far['Emergency'].append(data_dict['Emergency'][i])
            total_dict_so_far['Number of Incidents'].append(data_dict['Number of Incidents'][i])

    return total_dict_so_far


def get_covid_data(data: list[read.CovidData], location: str, year: int) -> dict[str, list]:
    """Return a dictionary of the covid data on the last day of each month for a specific year at a specific location

    Preconditions:
      - len(data) != 0
      - location in PROV_AND_TERR or location == 'Canada'
      - year >= 0
    """
    covid_in_location = get_monthly_cases(data, year, location)

    return covid_data_to_dict(covid_in_location)


# if __name__ == '__main__':
#     import python_ta
#     import python_ta.contracts
#
#     python_ta.contracts.DEBUG_CONTRACTS = False
#     python_ta.contracts.check_all_contracts()
#
#     python_ta.check_all(config={
#         'extra-imports': ['read'],  # the names (strs) of imported modules
#         'allowed-io': [],  # the names (strs) of functions that call print/open/input
#         'max-line-length': 120,
#         'disable': ['R1705', 'C0200']
#     })
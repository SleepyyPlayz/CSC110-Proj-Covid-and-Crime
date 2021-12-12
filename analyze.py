"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, Chris Jiang.
"""
import datetime

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
    """Return whether the CovidData instance is data for the last day of a certain month in a certain year for a
    particular location

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

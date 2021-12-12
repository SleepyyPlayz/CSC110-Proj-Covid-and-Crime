"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, Chris Jiang.
"""
import matplotlib
import pandas
import statsmodels

import read
import analyze

covid_data_raw = read.read_covid_data('data_sets/covid_data.csv')
police_data_raw = read.read_police_data('data_sets/police_data.csv')

# Covid Data for Canada for 2020
covid_data_canada_2020 = read.get_covid_data(covid_data_raw, 'Canada', 2020)

# Covid Data for Each Province for 2020
for pt in read.PROV_AND_TERR:
    covid_data_2020 = read.get_covid_data(covid_data_raw, pt, 2020)

# Covid Data for Canada for 2021
covid_data_canada_2021 = read.get_covid_data(covid_data_raw, 'Canada', 2021)

# Covid Data for Each Province for 2021
for pt in read.PROV_AND_TERR:
    covid_data_2021 = read.get_covid_data(covid_data_raw, pt, 2021)

# Physical and Non Physical Crimes for Canada for 2020
police_data_canada_2020_physical, police_data_canada_2020_non_physical = read.get_police_data(police_data_raw, 'Canada',
                                                                                              2020, 'physical')

# Public and Private Crimes for Canada for 2020
police_data_canada_2020_public, police_data_canada_2020_private = read.get_police_data(police_data_raw, 'Canada', 2020,
                                                                                       'public')

# Physical and Non Physical Crimes for Canada for 2021
police_data_canada_2021_physical, police_data_canada_2021_non_physical = read.get_police_data(police_data_raw, 'Canada',
                                                                                              2021, 'physical')

# Public and Private Crimes for Canada for 2021
police_data_canada_2021_public, police_data_canada_2021_private = read.get_police_data(police_data_raw, 'Canada', 2021,
                                                                                       'public')

# Total Physical and Non Physical Crimes for Canada for 2020
total_police_data_canada_2020_physical = read.get_police_data_totals(police_data_canada_2020_physical)
total_police_data_canada_2020_non_physical = read.get_police_data_totals(police_data_canada_2020_non_physical)

# Total Public and Private Crimes for Canada for 2020
total_police_data_canada_2020_public = read.get_police_data_totals(police_data_canada_2020_public)
total_police_data_canada_2020_private = read.get_police_data_totals(police_data_canada_2020_private)

# Total Physical and Non Physical Crimes for Canada for 2021
total_police_data_canada_2021_physical = read.get_police_data_totals(police_data_canada_2021_physical)
total_police_data_canada_2021_non_physical = read.get_police_data_totals(police_data_canada_2020_non_physical)

# Total Public and Private Crimes for Canada for 2021
total_police_data_canada_2021_public = read.get_police_data_totals(police_data_canada_2021_public)
total_police_data_canada_2021_private = read.get_police_data_totals(police_data_canada_2021_private)

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2020
for pt in read.PROV_AND_TERR:
    police_data_2020_physical, police_data_2020_non_physical = read.get_police_data(police_data_raw, pt, 2020,
                                                                                   'physical')
    total_police_data_2020_physical = read.get_police_data_totals(police_data_2020_physical)
    total_police_data_2020_non_phyiscal = read.get_police_data_totals(police_data_2020_non_physical)

# Public and Private Crimes (Total and Non-Total) for Each Province for 2020
for pt in read.PROV_AND_TERR:
    police_data_2020_public, police_data_2020_private = read.get_police_data(police_data_raw, pt, 2020, 'public')
    total_police_data_2020_public = read.get_police_data_totals(police_data_2020_public)
    total_police_data_2020_private = read.get_police_data_totals(police_data_2020_private)

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2021
for pt in read.PROV_AND_TERR:
    police_data_2021_physical, police_data_2021_non_physical = read.get_police_data(police_data_raw, pt, 2021,
                                                                                    'physical')
    total_police_data_2021_physical = read.get_police_data_totals(police_data_2021_physical)
    total_police_data_2021_non_physical = read.get_police_data_totals(police_data_2021_non_physical)

# Public and Private Crimes (Total and Non-Total) for Each Province for 2021
for pt in read.PROV_AND_TERR:
    police_data_2021_public, police_data_2021_private = read.get_police_data(police_data_raw, pt, 2021, 'public')
    total_police_data_2021_public = read.get_police_data_totals(police_data_2021_public)
    total_police_data_2021_private = read.get_police_data_totals(police_data_2021_private)

if __name__ == '__main__':
    from pprint import pprint
    pprint(covid_data_canada_2020)
    pprint(police_data_canada_2020_physical)
    pprint(total_police_data_canada_2020_physical)

"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""
import matplotlib as plt
import pandas as pd
import statsmodels

from pprint import pprint
import read
import analyze

covid_data_raw = read.read_covid_data('data_sets/covid_data.csv')
police_data_raw = read.read_police_data('data_sets/police_data.csv')

# Covid Data for Canada for 2020
covid_data_canada_2020 = analyze.get_covid_data(covid_data_raw, 'Canada', 2020)

# Covid Data for Each Province for 2020
for pt in read.PROV_AND_TERR:
    covid_data_2020 = analyze.get_covid_data(covid_data_raw, pt, 2020)

# Covid Data for Canada for 2021
covid_data_canada_2021 = analyze.get_covid_data(covid_data_raw, 'Canada', 2021)

# Covid Data for Each Province for 2021
for pt in read.PROV_AND_TERR:
    covid_data_2021 = analyze.get_covid_data(covid_data_raw, pt, 2021)

# THESE VARIABLES CONTAIN THE TOTALS OF INDIVIDUAL GROUPS OF CRIMES AND THE TOTAL OF INDIVIDUAL CRIMES
# THAT FALL UNDER THE SAME CATEGORY e.g. Assaults by family and Total assaults in that order
# COVERS WHOLE OF CANADA

# Physical and Non Physical Crimes for Canada for 2020
police_data_canada_2020_physical, police_data_canada_2020_non_physical = analyze.get_police_data(police_data_raw,
                                                                                                 'Canada', 2020,
                                                                                                 'physical')
# Public and Private Crimes for Canada for 2020
police_data_canada_2020_public, police_data_canada_2020_private = analyze.get_police_data(police_data_raw, 'Canada',
                                                                                          2020, 'public')

# Physical and Non Physical Crimes for Canada for 2021
police_data_canada_2021_physical, police_data_canada_2021_non_physical = analyze.get_police_data(police_data_raw,
                                                                                                 'Canada', 2021,
                                                                                                 'physical')
# Public and Private Crimes for Canada for 2021
police_data_canada_2021_public, police_data_canada_2021_private = analyze.get_police_data(police_data_raw, 'Canada',
                                                                                          2021, 'public')
# THESE VARIABLES CONTAIN JUST THE TOTALS OF INDIVIDUAL CRIMES THAT FALL UNDER THE SAME CATEGORY e.g.
# Total assaults
# COVERS WHOLE OF CANADA

# Total Physical and Non Physical Crimes for Canada for 2020
total_police_data_canada_2020_physical = analyze.get_police_data_totals(police_data_canada_2020_physical, 'Physical')
total_police_data_canada_2020_non_physical = analyze.get_police_data_totals(police_data_canada_2020_non_physical,
                                                                            'Non Physical')

# Total Public and Private Crimes for Canada for 2020
total_police_data_canada_2020_public = analyze.get_police_data_totals(police_data_canada_2020_public, 'Public')
total_police_data_canada_2020_private = analyze.get_police_data_totals(police_data_canada_2020_private, 'Private')

# Total Physical and Non Physical Crimes for Canada for 2021
total_police_data_canada_2021_physical = analyze.get_police_data_totals(police_data_canada_2021_physical, 'Physical')
total_police_data_canada_2021_non_physical = analyze.get_police_data_totals(police_data_canada_2020_non_physical,
                                                                            'Non Physical')

# Total Public and Private Crimes for Canada for 2021
total_police_data_canada_2021_public = analyze.get_police_data_totals(police_data_canada_2021_public, 'Public')
total_police_data_canada_2021_private = analyze.get_police_data_totals(police_data_canada_2021_private, 'Private')

# THESE VARIABLES CONTAIN THE TOTALS OF INDIVIDUAL GROUPS OF CRIMES AND THE TOTAL OF INDIVIDUAL CRIMES
# THAT FALL UNDER THE SAME CATEGORY e.g. Assaults by family and Total assaults in that order
# COVERS EACH PROVINCE

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2020
for pt in read.PROV_AND_TERR:
    police_data_2020_physical, police_data_2020_non_physical = analyze.get_police_data(police_data_raw, pt, 2020,
                                                                                       'physical')
    total_police_data_2020_physical = analyze.get_police_data_totals(police_data_2020_physical, 'Physical')
    total_police_data_2020_non_physical = analyze.get_police_data_totals(police_data_2020_non_physical, 'Non Physical')

# Public and Private Crimes (Total and Non-Total) for Each Province for 2020
for pt in read.PROV_AND_TERR:
    police_data_2020_public, police_data_2020_private = analyze.get_police_data(police_data_raw, pt, 2020, 'public')
    total_police_data_2020_public = analyze.get_police_data_totals(police_data_2020_public, 'Public')
    total_police_data_2020_private = analyze.get_police_data_totals(police_data_2020_private, 'Private')

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2021
for pt in read.PROV_AND_TERR:
    police_data_2021_physical, police_data_2021_non_physical = analyze.get_police_data(police_data_raw, pt, 2021,
                                                                                       'physical')
    total_police_data_2021_physical = analyze.get_police_data_totals(police_data_2021_physical, 'Physical')
    total_police_data_2021_non_physical = analyze.get_police_data_totals(police_data_2021_non_physical, 'Non Physical')

# Public and Private Crimes (Total and Non-Total) for Each Province for 2021
for pt in read.PROV_AND_TERR:
    police_data_2021_public, police_data_2021_private = analyze.get_police_data(police_data_raw, pt, 2021, 'public')
    total_police_data_2021_public = analyze.get_police_data_totals(police_data_2021_public, 'Public')
    total_police_data_2021_private = analyze.get_police_data_totals(police_data_2021_private, 'Private')

if __name__ == '__main__':
    from pprint import pprint
    # pprint(covid_data_canada_2020)
    # pprint(police_data_canada_2020_physical)
    # pprint(total_police_data_canada_2020_physical)


# STEP 1: Creating a Pandas Data Frame for Everything

########################## COVID DATASET ##########################################################

# Covid Data Frame for Canada for 2020
covid_data_canada_2020_df = pd.DataFrame(covid_data_canada_2020)

# Creating a list of Covid Data Frames for Each Province for Covid Data 2020,
df_list_per_province_covid_data_2020  = []
for pt in read.PROV_AND_TERR:
    covid_data_2020 = analyze.get_covid_data(covid_data_raw, pt, 2020)
    covid_data_2020_df = pd.DataFrame(covid_data_2020)
    df_list_per_province_covid_data_2020.append(covid_data_2020_df)

# Covid Data Frame for Canada for 2021
covid_data_canada_2021_df = pd.DataFrame(covid_data_canada_2021)

# Creating a list of Covid Data Frames for Each Province for Covid Data 2020,
df_list_per_province_covid_data_2021 = []
for pt in read.PROV_AND_TERR:
    covid_data_2021 = analyze.get_covid_data(covid_data_raw, pt, 2021)
    covid_data_2021_df = pd.DataFrame(covid_data_2021)
    df_list_per_province_covid_data_2021.append(covid_data_2021_df)

########################## CRIME DATASET ##########################################################

# Physical and Non Physical Crimes for Canada for 2020 Data Frame
police_data_canada_2020_physical_df = pd.DataFrame(police_data_canada_2020_physical)
police_data_canada_2020_non_physical_df = pd.DataFrame(police_data_canada_2020_non_physical)

# Public and Private Crimes for Canada for 2020 Data Frame
police_data_canada_2020_public_df = pd.DataFrame(police_data_canada_2020_public)
police_data_canada_2020_private_df = pd.DataFrame(police_data_canada_2020_private)

# Physical and Non Physical Crimes for Canada for 2021 Data Frame
police_data_canada_2021_physical_df = pd.DataFrame(police_data_canada_2021_physical)
police_data_canada_2021_non_physical_df = pd.DataFrame(police_data_canada_2021_physical)

# Public and Private Crimes for Canada for 2021 Data Frame
police_data_canada_2021_public_df = pd.DataFrame(police_data_canada_2021_public)
police_data_canada_2021_private_df = pd.DataFrame(police_data_canada_2021_private)

# Total Physical and Non Physical Crimes for Canada for 2020 Data Frame
total_police_data_canada_2020_physical_df = pd.DataFrame(total_police_data_canada_2020_physical)
total_police_data_canada_2020_non_physical_df = pd.DataFrame(total_police_data_canada_2020_non_physical)

# Total Public and Private Crimes for Canada for 2020 Data Frame
total_police_data_canada_2020_public_df = pd.DataFrame(total_police_data_canada_2020_public)
total_police_data_canada_2020_private_df = pd.DataFrame(total_police_data_canada_2020_private)

# Total Physical and Non Physical Crimes for Canada for 2021 Data Frame
total_police_data_canada_2021_physical_df = pd.DataFrame(total_police_data_canada_2021_physical)
total_police_data_canada_2021_non_physical_df = pd.DataFrame(total_police_data_canada_2021_non_physical)

# Total Public and Private Crimes for Canada for 2021 Data Frame
total_police_data_canada_2021_public_df = pd.DataFrame(total_police_data_canada_2021_public)
total_police_data_canada_2021_private_df = pd.DataFrame(total_police_data_canada_2021_private)

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2020 Data Frame
df_list_per_province_police_data_2020_physical = []
df_list_per_province_police_data_2020_non_physical = []
df_list_per_province_total_police_data_2020_physical = []
df_list_per_province_total_police_data_2020_non_physical = []

for pt in read.PROV_AND_TERR:
    police_data_2020_physical, police_data_2020_non_physical = analyze.get_police_data(police_data_raw, pt, 2020,
                                                                                       'physical')
    total_police_data_2020_physical = analyze.get_police_data_totals(police_data_2020_physical)
    total_police_data_2020_non_physical = analyze.get_police_data_totals(police_data_2020_non_physical)

    police_data_2020_physical_df = pd.DataFrame(police_data_2020_physical)
    police_data_2020_non_physical_df = pd.DataFrame(police_data_2020_non_physical)
    total_police_data_2020_physical_df = pd.DataFrame(total_police_data_2020_physical)
    total_police_data_2020_non_physical_df = pd.DataFrame(total_police_data_2020_non_physical)

    df_list_per_province_police_data_2020_physical.append(police_data_2020_physical_df)
    df_list_per_province_police_data_2020_non_physical.append(police_data_2020_non_physical_df)
    df_list_per_province_total_police_data_2020_physical.append(total_police_data_2020_physical_df)
    df_list_per_province_total_police_data_2020_non_physical.append(total_police_data_2020_non_physical_df)

# Public and Private Crimes (Total and Non-Total) for Each Province for 2020 Data Frame
df_list_per_province_police_data_2020_public = []
df_list_per_province_police_data_2020_private = []
df_list_per_province_total_police_data_2020_public = []
df_list_per_province_total_police_data_2020_private = []
for pt in read.PROV_AND_TERR:
    police_data_2020_public, police_data_2020_private = analyze.get_police_data(police_data_raw, pt, 2020, 'public')
    total_police_data_2020_public = analyze.get_police_data_totals(police_data_2020_public)
    total_police_data_2020_private = analyze.get_police_data_totals(police_data_2020_private)

    police_data_2020_public_df = pd.DataFrame(police_data_2020_public)
    police_data_2020_private_df = pd.DataFrame(police_data_2020_private)
    total_police_data_2020_public_df = pd.DataFrame(total_police_data_2020_public)
    total_police_data_2020_private_df = pd.DataFrame(total_police_data_2020_private)

    df_list_per_province_police_data_2020_public.append(police_data_2020_public_df)
    df_list_per_province_police_data_2020_private.append(police_data_2020_private_df)
    df_list_per_province_total_police_data_2020_public.append(total_police_data_2020_public_df)
    df_list_per_province_total_police_data_2020_private.append(total_police_data_2020_private_df)

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2021 Data Frame
df_list_per_province_police_data_2021_physical = []
df_list_per_province_police_data_2021_non_physical = []
df_list_per_province_total_police_data_2021_physical = []
df_list_per_province_total_police_data_2021_non_physical = []
for pt in read.PROV_AND_TERR:
    police_data_2021_physical, police_data_2021_non_physical = analyze.get_police_data(police_data_raw, pt, 2021,
                                                                                       'physical')
    total_police_data_2021_physical = analyze.get_police_data_totals(police_data_2021_physical)
    total_police_data_2021_non_physical = analyze.get_police_data_totals(police_data_2021_non_physical)

    police_data_2021_physical_df = pd.DataFrame(police_data_2021_physical)
    police_data_2021_non_physical_df = pd.DataFrame(police_data_2021_non_physical)
    total_police_data_2021_physical_df = pd.DataFrame(total_police_data_2021_physical)
    total_police_data_2021_non_physical_df = pd.DataFrame(total_police_data_2021_non_physical)

    df_list_per_province_police_data_2021_physical.append(police_data_2021_physical_df)
    df_list_per_province_police_data_2021_non_physical.append(police_data_2021_non_physical_df)
    df_list_per_province_total_police_data_2021_physical.append(total_police_data_2021_physical_df)
    df_list_per_province_total_police_data_2021_non_physical.append(total_police_data_2021_non_physical_df)

# Public and Private Crimes (Total and Non-Total) for Each Province for 2021 Data Frame
df_list_per_province_police_data_2021_public = []
df_list_per_province_police_data_2021_private = []
df_list_per_province_total_police_data_2021_public = []
df_list_per_province_total_police_data_2021_private = []
for pt in read.PROV_AND_TERR:
    police_data_2021_public, police_data_2021_private = analyze.get_police_data(police_data_raw, pt, 2021, 'public')
    total_police_data_2021_public = analyze.get_police_data_totals(police_data_2021_public)
    total_police_data_2021_private = analyze.get_police_data_totals(police_data_2021_private)

    police_data_2021_public_df = pd.DataFrame(police_data_2021_public)
    police_data_2021_private_df = pd.DataFrame(police_data_2021_private)
    total_police_data_2021_public_df = pd.DataFrame(total_police_data_2021_public)
    total_police_data_2021_private_df = pd.DataFrame(total_police_data_2021_private)

    df_list_per_province_police_data_2021_public.append(police_data_2021_public_df)
    df_list_per_province_police_data_2021_private.append(police_data_2021_private_df)
    df_list_per_province_total_police_data_2021_public.append(total_police_data_2021_public_df)
    df_list_per_province_total_police_data_2021_private.append(total_police_data_2021_private_df)



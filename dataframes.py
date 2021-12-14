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

COVID_DATA_RAW = read.read_covid_data('data_sets/covid_data.csv')
POLICE_DATA_RAW = read.read_police_data('data_sets/police_data.csv')

# Covid Data for Canada for 2020
covid_data_canada_2020 = analyze.get_covid_data(COVID_DATA_RAW, 'Canada', 2020)

# Covid Data for Each Province for 2020
for pt in read.PROV_AND_TERR:
    covid_data_2020 = analyze.get_covid_data(COVID_DATA_RAW, pt, 2020)

# Covid Data for Canada for 2021
covid_data_canada_2021 = analyze.get_covid_data(COVID_DATA_RAW, 'Canada', 2021)

# Covid Data for Each Province for 2021
for pt in read.PROV_AND_TERR:
    covid_data_2021 = analyze.get_covid_data(COVID_DATA_RAW, pt, 2021)

# THESE VARIABLES CONTAIN THE TOTALS OF INDIVIDUAL GROUPS OF CRIMES AND THE TOTAL OF INDIVIDUAL CRIMES
# THAT FALL UNDER THE SAME CATEGORY e.g. Assaults by family and Total assaults in that order
# COVERS WHOLE OF CANADA

# Physical and Non Physical Crimes for Canada for 2020
police_data_canada_2020_physical, police_data_canada_2020_non_physical = analyze.get_police_data(POLICE_DATA_RAW,
                                                                                                 'Canada', 2020,
                                                                                                 'physical')
# Public and Private Crimes for Canada for 2020
police_data_canada_2020_public, police_data_canada_2020_private = analyze.get_police_data(POLICE_DATA_RAW, 'Canada',
                                                                                          2020, 'public')

# Physical and Non Physical Crimes for Canada for 2021
police_data_canada_2021_physical, police_data_canada_2021_non_physical = analyze.get_police_data(POLICE_DATA_RAW,
                                                                                                 'Canada', 2021,
                                                                                                 'physical')
# Public and Private Crimes for Canada for 2021
police_data_canada_2021_public, police_data_canada_2021_private = analyze.get_police_data(POLICE_DATA_RAW, 'Canada',
                                                                                          2021, 'public')
# THESE VARIABLES CONTAIN JUST THE TOTALS OF INDIVIDUAL CRIMES THAT FALL UNDER THE SAME CATEGORY e.g.
# Total assaults
# COVERS WHOLE OF CANADA

# Total Physical and Non Physical Crimes for Canada for 2020
total_police_data_canada_2020_physical = analyze.get_police_data_totals(police_data_canada_2020_physical, 'Physical',
                                                                        2020, 'Canada')
total_police_data_canada_2020_non_physical = analyze.get_police_data_totals(police_data_canada_2020_non_physical,
                                                                            'Non Physical', 2020, 'Canada')

# Total Public and Private Crimes for Canada for 2020
total_police_data_canada_2020_public = analyze.get_police_data_totals(police_data_canada_2020_public, 'Public', 2020,
                                                                      'Canada')
total_police_data_canada_2020_private = analyze.get_police_data_totals(police_data_canada_2020_private, 'Private', 2020,
                                                                       'Canada')

# Total Physical and Non Physical Crimes for Canada for 2021
total_police_data_canada_2021_physical = analyze.get_police_data_totals(police_data_canada_2021_physical, 'Physical',
                                                                        2021, 'Canada')
total_police_data_canada_2021_non_physical = analyze.get_police_data_totals(police_data_canada_2020_non_physical,
                                                                            'Non Physical', 2021, 'Canada')

# Total Public and Private Crimes for Canada for 2021
total_police_data_canada_2021_public = analyze.get_police_data_totals(police_data_canada_2021_public, 'Public', 2021,
                                                                      'Canada')
total_police_data_canada_2021_private = analyze.get_police_data_totals(police_data_canada_2021_private, 'Private', 2021,
                                                                       'Canada')

# THESE VARIABLES CONTAIN THE TOTALS OF INDIVIDUAL GROUPS OF CRIMES AND THE TOTAL OF INDIVIDUAL CRIMES
# THAT FALL UNDER THE SAME CATEGORY e.g. Assaults by family and Total assaults in that order
# COVERS EACH PROVINCE

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2020
for pt in read.PROV_AND_TERR:
    police_data_2020_physical, police_data_2020_non_physical = analyze.get_police_data(POLICE_DATA_RAW, pt, 2020,
                                                                                       'physical')
    total_police_data_2020_physical = analyze.get_police_data_totals(police_data_2020_physical, 'Physical', 2020, pt)
    total_police_data_2020_non_physical = analyze.get_police_data_totals(police_data_2020_non_physical, 'Non Physical',
                                                                         2020, pt)

# Public and Private Crimes (Total and Non-Total) for Each Province for 2020
for pt in read.PROV_AND_TERR:
    police_data_2020_public, police_data_2020_private = analyze.get_police_data(POLICE_DATA_RAW, pt, 2020, 'public')
    total_police_data_2020_public = analyze.get_police_data_totals(police_data_2020_public, 'Public', 2020, pt)
    total_police_data_2020_private = analyze.get_police_data_totals(police_data_2020_private, 'Private', 2020, pt)

# Physical and Non Physical Crimes (Total and Non-Total) for Each Province for 2021
for pt in read.PROV_AND_TERR:
    police_data_2021_physical, police_data_2021_non_physical = analyze.get_police_data(POLICE_DATA_RAW, pt, 2021,
                                                                                       'physical')
    total_police_data_2021_physical = analyze.get_police_data_totals(police_data_2021_physical, 'Physical', 2021, pt)
    total_police_data_2021_non_physical = analyze.get_police_data_totals(police_data_2021_non_physical, 'Non Physical',
                                                                         2021, pt)

# Public and Private Crimes (Total and Non-Total) for Each Province for 2021
for pt in read.PROV_AND_TERR:
    police_data_2021_public, police_data_2021_private = analyze.get_police_data(POLICE_DATA_RAW, pt, 2021, 'public')
    total_police_data_2021_public = analyze.get_police_data_totals(police_data_2021_public, 'Public', 2021, pt)
    total_police_data_2021_private = analyze.get_police_data_totals(police_data_2021_private, 'Private', 2021, pt)

# CREATING PANDAS DATAFRAMES

# ------------------------------------- COVID DATASET DATA FRAME-------------------------------- #

# Covid Data Frame for Canada for 2020
covid_data_canada_2020_df = pd.DataFrame(covid_data_canada_2020)

# Covid Data Frame for Canada for 2021
covid_data_canada_2021_df = pd.DataFrame(covid_data_canada_2021)

# Creating a list of Covid Data Frames for Each Province for Covid Data 2020,
df_list_per_province_covid_data_2020 = []
for pt in read.PROV_AND_TERR:
    covid_data_2020 = analyze.get_covid_data(COVID_DATA_RAW, pt, 2020)
    covid_data_2020_df = pd.DataFrame(covid_data_2020)
    df_list_per_province_covid_data_2020.append(covid_data_2020_df)

# Creating a list of Covid Data Frames for Each Province for Covid Data 2021,
df_list_per_province_covid_data_2021 = []
for pt in read.PROV_AND_TERR:
    covid_data_2021 = analyze.get_covid_data(COVID_DATA_RAW, pt, 2021)
    covid_data_2021_df = pd.DataFrame(covid_data_2021)
    df_list_per_province_covid_data_2021.append(covid_data_2021_df)

# ----------------------------------------- CRIME DATASET DATA FRAME ---------------------------- #

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

# Total Physical and Total Non Physical Crimes for Each Province for 2020 Data Frame
df_list_per_province_total_police_data_2020_physical = []
df_list_per_province_total_police_data_2020_non_physical = []
for pt in read.PROV_AND_TERR:
    police_data_2020_physical, police_data_2020_non_physical = analyze.get_police_data(POLICE_DATA_RAW, pt, 2020,
                                                                                       'physical')
    total_police_data_2020_physical = analyze.get_police_data_totals(police_data_2020_physical, 'Physical', 2020, pt)
    total_police_data_2020_non_physical = analyze.get_police_data_totals(police_data_2020_non_physical, 'Non Physical',
                                                                         2020, pt)

    total_police_data_2020_physical_df = pd.DataFrame(total_police_data_2020_physical)
    total_police_data_2020_non_physical_df = pd.DataFrame(total_police_data_2020_non_physical)

    df_list_per_province_total_police_data_2020_physical.append(total_police_data_2020_physical_df)
    df_list_per_province_total_police_data_2020_non_physical.append(total_police_data_2020_non_physical_df)

# Total Public and Total Private Crimes for Each Province for 2020 Data Frame
df_list_per_province_total_police_data_2020_public = []
df_list_per_province_total_police_data_2020_private = []
for pt in read.PROV_AND_TERR:
    police_data_2020_public, police_data_2020_private = analyze.get_police_data(POLICE_DATA_RAW, pt, 2020, 'public')
    total_police_data_2020_public = analyze.get_police_data_totals(police_data_2020_public, 'Public', 2020, pt)
    total_police_data_2020_private = analyze.get_police_data_totals(police_data_2020_private, 'Private', 2020, pt)

    total_police_data_2020_public_df = pd.DataFrame(total_police_data_2020_public)
    total_police_data_2020_private_df = pd.DataFrame(total_police_data_2020_private)

    df_list_per_province_total_police_data_2020_public.append(total_police_data_2020_public_df)
    df_list_per_province_total_police_data_2020_private.append(total_police_data_2020_private_df)

# Total Physical and Total Non Physical Crimes for Each Province for 2021 Data Frame
df_list_per_province_total_police_data_2021_physical = []
df_list_per_province_total_police_data_2021_non_physical = []
for pt in read.PROV_AND_TERR:
    police_data_2021_physical, police_data_2021_non_physical = analyze.get_police_data(POLICE_DATA_RAW, pt, 2021,
                                                                                       'physical')
    total_police_data_2021_physical = analyze.get_police_data_totals(police_data_2021_physical, 'Physical', 2021, pt)
    total_police_data_2021_non_physical = analyze.get_police_data_totals(police_data_2021_non_physical, 'Non Physical',
                                                                         2021, pt)

    total_police_data_2021_physical_df = pd.DataFrame(total_police_data_2021_physical)
    total_police_data_2021_non_physical_df = pd.DataFrame(total_police_data_2021_non_physical)

    df_list_per_province_total_police_data_2021_physical.append(total_police_data_2021_physical_df)
    df_list_per_province_total_police_data_2021_non_physical.append(total_police_data_2021_non_physical_df)

# Total Public and Total Private Crimes for Each Province for 2021 Data Frame
df_list_per_province_total_police_data_2021_public = []
df_list_per_province_total_police_data_2021_private = []
for pt in read.PROV_AND_TERR:
    police_data_2021_public, police_data_2021_private = analyze.get_police_data(POLICE_DATA_RAW, pt, 2021, 'public')
    total_police_data_2021_public = analyze.get_police_data_totals(police_data_2021_public, 'Public', 2021, pt)
    total_police_data_2021_private = analyze.get_police_data_totals(police_data_2021_private, 'Private', 2021, pt)

    total_police_data_2021_public_df = pd.DataFrame(total_police_data_2021_public)
    total_police_data_2021_private_df = pd.DataFrame(total_police_data_2021_private)

    df_list_per_province_total_police_data_2021_public.append(total_police_data_2021_public_df)
    df_list_per_province_total_police_data_2021_private.append(total_police_data_2021_private_df)

# ------------------------------  COMBINING THE CANADA COVID DATA FRAME ------------------------- #
covid_data_canada_20_21_df = covid_data_canada_2020_df.append(covid_data_canada_2021_df)



# ------------------------------  COMBINING THE PROVINCE DATA FRAMES----------------------------- #

# ------------------------------  COVID DATASET --------------------------------- #

# Creating a combined Covid Data Frame for Each Province for Covid Data 2020,
final_df_list_per_province_covid_data_2020 = df_list_per_province_covid_data_2020[0]
for df in df_list_per_province_covid_data_2020[1:]:
    final_df_list_per_province_covid_data_2020 = \
        pd.merge(final_df_list_per_province_covid_data_2020, df, on="Date")

# Creating a combined Covid Data Frame for Each Province for Covid Data 2021,
final_df_list_per_province_covid_data_2021 = df_list_per_province_covid_data_2021[0]
for df in df_list_per_province_covid_data_2021[1:]:
    final_df_list_per_province_covid_data_2021 = \
        pd.merge(final_df_list_per_province_covid_data_2021, df, on="Date")

# ------------------------------  CRIME DATASET 2020 --------------------------------- #

# Combined Data Frame for Total Physical Crimes for Each Province for 2020
final_df_list_per_province_total_police_data_2020_physical = \
    df_list_per_province_total_police_data_2020_physical[0]
for df in df_list_per_province_total_police_data_2020_physical[1:]:
    final_df_list_per_province_total_police_data_2020_physical = \
        pd.merge(final_df_list_per_province_total_police_data_2020_physical, df, on="Date")

# Combined Data Frame for Total Non Physical Crimes for Each Province for 2020
final_df_list_per_province_total_police_data_2020_non_physical = \
    df_list_per_province_total_police_data_2020_non_physical[0]
for df in df_list_per_province_total_police_data_2020_non_physical[1:]:
    final_df_list_per_province_total_police_data_2020_non_physical = \
        pd.merge(final_df_list_per_province_total_police_data_2020_non_physical, df, on="Date")

# Combined Data Frame for Total Public Crimes for Each Province for 2020
final_df_list_per_province_total_police_data_2020_public = \
    df_list_per_province_total_police_data_2020_public[0]
for df in df_list_per_province_total_police_data_2020_public[1:]:
    final_df_list_per_province_total_police_data_2020_public = \
        pd.merge(final_df_list_per_province_total_police_data_2020_public, df, on="Date")

# Combined Data Frame for Total Private Crimes for Each Province for 2020
final_df_list_per_province_total_police_data_2020_private = \
    df_list_per_province_total_police_data_2020_private[0]
for df in df_list_per_province_total_police_data_2020_private[1:]:
    final_df_list_per_province_total_police_data_2020_private = \
        pd.merge(final_df_list_per_province_total_police_data_2020_private, df, on="Date")

# ------------------------------  CRIME DATASET 2021 --------------------------------- #

# Combined Data Frame for Total Physical Crimes for Each Province for 2021
final_df_list_per_province_total_police_data_2021_physical = \
    df_list_per_province_total_police_data_2021_physical[0]
for df in df_list_per_province_total_police_data_2021_physical[1:]:
    final_df_list_per_province_total_police_data_2021_physical = \
        pd.merge(final_df_list_per_province_total_police_data_2021_physical, df, on="Date")

# Combined Data Frame for Total Non Physical Crimes for Each Province for 2021
final_df_list_per_province_total_police_data_2021_non_physical = \
    df_list_per_province_total_police_data_2021_non_physical[0]
for df in df_list_per_province_total_police_data_2021_non_physical[1:]:
    final_df_list_per_province_total_police_data_2021_non_physical = \
        pd.merge(final_df_list_per_province_total_police_data_2021_non_physical, df, on="Date")

# Combined Data Frame for Total Public Crimes for Each Province for 2021
final_df_list_per_province_total_police_data_2021_public = \
    df_list_per_province_total_police_data_2021_public[0]
for df in df_list_per_province_total_police_data_2021_public[1:]:
    final_df_list_per_province_total_police_data_2021_public = \
        pd.merge(final_df_list_per_province_total_police_data_2021_public, df, on="Date")

# Combined Data Frame for Total Private Crimes for Each Province for 2021
final_df_list_per_province_total_police_data_2021_private = \
    df_list_per_province_total_police_data_2021_private[0]
for df in df_list_per_province_total_police_data_2021_private[1:]:
    final_df_list_per_province_total_police_data_2021_private = \
        pd.merge(final_df_list_per_province_total_police_data_2021_private, df, on="Date")

# ------------------------- 2020 AND 2021 CRIME DATA FRAMES COMBINED ---------------------------- #
total_police_data_canada_20_21_physical_df = total_police_data_canada_2020_physical_df.append(
    total_police_data_canada_2021_physical_df
)

total_police_data_canada_20_21_non_physical_df = total_police_data_canada_2020_non_physical_df.append(
    total_police_data_canada_2021_non_physical_df
)

total_police_data_canada_20_21_public_df = total_police_data_canada_2020_public_df.append(
    total_police_data_canada_2021_public_df
)

total_police_data_canada_20_21_private_df = total_police_data_canada_2020_private_df.append(
    total_police_data_canada_2021_private_df
)

final_df_per_province_total_police_data_20_21_physical = \
    final_df_list_per_province_total_police_data_2020_physical.append(
        final_df_list_per_province_total_police_data_2021_physical)

final_df_per_province_total_police_data_20_21_non_physical = \
    final_df_list_per_province_total_police_data_2020_non_physical.append(
        final_df_list_per_province_total_police_data_2021_non_physical)

final_df_per_province_total_police_data_20_21_public = \
    final_df_list_per_province_total_police_data_2020_public.append(
        final_df_list_per_province_total_police_data_2021_public)

final_df_per_province_total_police_data_20_21_private = \
    final_df_list_per_province_total_police_data_2020_private.append(
        final_df_list_per_province_total_police_data_2021_private)

# ------------------------------------- MAIN RUNNING SECTION --------------------------------- #

if __name__ == '__main__':
    from pprint import pprint
    pprint(covid_data_canada_20_21_df)
    pprint(covid_data_canada_20_21_df.info())
    #pprint(total_police_data_canada_20_21_private_df.tail())
    #pprint(total_police_data_canada_20_21_private_df.info())

    # pprint(covid_data_canada_2020)
    # pprint(police_data_canada_2020_physical)
    # pprint(total_police_data_canada_2020_physical)

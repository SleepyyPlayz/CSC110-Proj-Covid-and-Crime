"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""
import tkinter as tk, dataframes as df
import matplotlib.pyplot as plt

PROV_AND_TERR = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec',
                 'Newfoundland and Labrador', 'New Brunswick', 'Nova Scotia', 'Prince Edward Island',
                 'Northwest Territories', 'Nunavut', 'Yukon']

# Covid Cases Graph for Canada for 2020 and 2021
date_20_21 = df.covid_data_canada_20_21_df['Date']
cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
covid_canada_20_21 = plt.figure()
covid_canada_20_21_axes = covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
covid_canada_20_21_axes.plot(date_20_21, cases_20_21)

# Covid Cases per Province Graph for Canada for 2020 and 2021

# Graph for Total Physical Crimes for Each Province for 2020

# date_20_21 = df.covid_data_canada_20_21_df['Date']
# cases_20_21 = df.covid_data_canada_20_21_df['Number of Active Cases in Canada']
# covid_canada_20_21 = plt.figure()
# covid_canada_20_21_axes = covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# covid_canada_20_21_axes.plot(date_20_21, cases_20_21)



# Total Physical Crimes Canada 2020 Graph
# date_2020 = df.covid_data_canada_2020_df['Date']
# physical_crimes_2020 = df.total_police_data_canada_2020_physical_df['Total Physical Crimes in Canada']
# physical_crimes_2020 = plt.plot_date(date_2020, physical_crimes_2020, linestyle='solid')

# Total Physical Crimes Canada 2021 Graph

# ------------------------------  Graph Formatting + Necessary Code ----------------------------- #


# ------------------------------------- MAIN RUNNING SECTION --------------------------------- #
if __name__ == '__main__':
    from pprint import pprint
    #print(physical_crimes_2020)
    #print(covid_canada_2021)




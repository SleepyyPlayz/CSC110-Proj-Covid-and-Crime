"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""

# import tkinter as tk
import dataframes as df
import matplotlib.pyplot as plt

# Covid Cases Graph for Canada for 2020 and 2021
# date_20_21 = df.covid_data_canada_20_21_df['Date']
cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']

# physical_covid_canada_20_21 = plt.figure()
# covid_canada_20_21_axes = physical_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# covid_canada_20_21_axes.plot(date_20_21, cases_20_21)

# Total PHYSICAL Crimes Graph for Canada for 2020 and 2021
physical_covid_canada_20_21 = plt.figure()
physical_covid_canada_20_21_axes = physical_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
physical_crimes_20_21 = df.total_police_data_canada_20_21_physical_df['Total Physical Crimes in Canada']
# date_20_21 = df.total_police_data_canada_20_21_physical_df['Date']
physical_covid_canada_20_21_axes.scatter(cases_20_21, physical_crimes_20_21.iloc[0:20])
physical_covid_canada_20_21_axes.set_title("Covid -> Total Physical Crime")

# Total NON PHYSICAL Crimes Graph for Canada for 2020 and 2021
non_physical_covid_canada_20_21 = plt.figure()
non_physical_covid_canada_20_21_axes = non_physical_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
non_physical_crimes_20_21 = \
    df.total_police_data_canada_20_21_non_physical_df['Total Non Physical Crimes in Canada']
# date_20_21 = df.total_police_data_canada_20_21_non_physical_df['Date']
non_physical_covid_canada_20_21_axes.scatter(cases_20_21, non_physical_crimes_20_21.iloc[0:20])
non_physical_covid_canada_20_21_axes.set_title("Covid -> Total Non-Physical Crime")

# Total PUBLIC Crimes Graph for Canada for 2020 and 2021
public_covid_canada_20_21 = plt.figure()
public_covid_canada_20_21_axes = public_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
public_crimes_20_21 = \
    df.total_police_data_canada_20_21_public_df['Total Public Crimes in Canada']
# date_20_21 = df.total_police_data_canada_20_21_public_df['Date']
public_covid_canada_20_21_axes.scatter(cases_20_21, public_crimes_20_21.iloc[0:20])
public_covid_canada_20_21_axes.set_title("Covid -> Total Public Crime")

# Total PRIVATE Crimes Graph for Canada for 2020 and 2021
private_covid_canada_20_21 = plt.figure()
private_covid_canada_20_21_axes = private_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
private_crimes_20_21 = \
    df.total_police_data_canada_20_21_private_df['Total Private Crimes in Canada']
# date_20_21 = df.total_police_data_canada_20_21_private_df['Date']
private_covid_canada_20_21_axes.scatter(cases_20_21, private_crimes_20_21.iloc[0:20])
private_covid_canada_20_21_axes.set_title("Covid -> Total Private Crime")

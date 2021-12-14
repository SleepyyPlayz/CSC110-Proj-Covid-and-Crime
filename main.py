"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""
import tkinter as tk, dataframes as df
from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt

# # Covid Cases Graph for Canada for 2020
# date_2020 = df.covid_data_canada_2020_df['Date']
# cases_2020 = df.covid_data_canada_2020_df['Number of Active Cases in Canada']
# covid_canada_2020 = plt.plot_date(date_2020, cases_2020, linestyle = 'solid' )
#
# # Covid Cases Graph for Canada for 2021
# date_2021 = df.covid_data_canada_2021_df['Date']
# cases_2021 = df.covid_data_canada_2021_df['Number of Active Cases in Canada']
# covid_canada_2021 = plt.plot_date(date_2021, cases_2021, linestyle='solid')
#
# # Total Physical Crimes Canada 2020 Graph
# physical_crimes_2020 = df.total_police_data_canada_2020_physical_df['Total Physical Crimes in Canada']
# physical_crimes_2020 = plt.plot_date(date_2020, physical_crimes_2020, linestyle='solid')
# # Total Physical Crimes Canada 2021 Graph
#
# # ------------------------------  Graph Formatting + Necessary Code ----------------------------- #
# plt.style.use('seaborn')
# plt.legend()
# plt.grid()
# plt.figure()

# To begin with, we create a figure instance which provides an empty canvas.
fig = plt.figure()
ax = fig.add_axes([0, 0, 0.5, 0.5])
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()

# ------------------------------------- MAIN RUNNING SECTION --------------------------------- #
if __name__ == '__main__':
    from pprint import pprint
    #print(physical_crimes_2020)
    #print(covid_canada_2021)

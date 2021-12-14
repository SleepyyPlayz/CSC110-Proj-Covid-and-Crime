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
# date_20_21 = df.covid_data_canada_20_21_df['Date']
# cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
# physical_crimes_20_21 = df.total_police_data_canada_20_21_physical_df['Total Physical Crimes in Canada']
#
# covid_crime_canada_20_21 = plt.figure()

#covid_canada_20_21_axes = covid_crime_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# fig = plt.figure()
# physical_crimes_canada_20_21_axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

#covid_canada_20_21_axes.plot(date_20_21, cases_20_21)
# date_20_21 = df.total_police_data_canada_20_21_non_physical_df['Date']
# physical_crimes_canada_20_21_axes.plot(date_20_21, physical_crimes_20_21)

# Total Physical Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_physical_df['Date']

# physical_crimes_canada_20_21 = plt.figure(1)

#covid_canada_20_21_axes.plot(date_20_21, physical_crimes_20_21)

# Total Non Physical Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_non_physical_df['Date']
# non_physical_crimes_20_21 = \
#      df.total_police_data_canada_20_21_non_physical_df['Total Non Physical Crimes in Canada']
# non_physical_crimes_canada_20_21 = plt.figure()
# non_physical_crimes_canada_20_21_axes = non_physical_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# non_physical_crimes_canada_20_21_axes.plot(date_20_21, non_physical_crimes_20_21)

# Total Public Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_public_df['Date']
# public_crimes_20_21 = \
#      df.total_police_data_canada_20_21_public_df['Total Public Crimes in Canada']
# public_crimes_canada_20_21 = plt.figure()
# public_crimes_canada_20_21_axes = public_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# public_crimes_canada_20_21_axes.plot(date_20_21, public_crimes_20_21)

# Total Private Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_private_df['Date']
# private_crimes_20_21 = \
#      df.total_police_data_canada_20_21_private_df['Total Private Crimes in Canada']
# private_crimes_canada_20_21 = plt.figure()
# private_crimes_canada_20_21_axes = private_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# private_crimes_canada_20_21_axes.plot(date_20_21, private_crimes_20_21)



# Graph name, x axes label, y axes label, wrapper, colour, legend
#------------------------------------------------------------------------------------#
# Covid Cases per Province Graph for Canada for 2020 and 2021

# ---------------------------- Tkinter Program -------------------------------------------------- #
root = tk.Tk()
root.title('Visualizing Covid Data')
root.geometry('900x300')
root.configure(background="#FFFFFF")

title_font = ("Arial", 16, "bold")
paragraph_font = ("Arial", 12, "normal")

frame_heading_1 = tk.Label(root, text = "Visualising the relationship between Total Covid Cases in Canada and "
                                                     "Crime Rates", font = title_font)
frame_heading_1.grid(row=0, column=0, columnspan = "15", sticky = "W")

def canada_covid_crime():
    date_20_21 = df.covid_data_canada_20_21_df['Date']
    cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
    physical_20_21 = df.total_police_data_canada_20_21_physical_df['Total Physical Crimes in Canada']
    non_physical_20_21 = df.total_police_data_canada_20_21_non_physical_df['Total Non Physical Crimes in Canada']
    public_axes_20_21 = df.total_police_data_canada_20_21_public_df['Total Public Crimes in Canada']
    private_axes_20_21 = df.total_police_data_canada_20_21_private_df['Total Private Crimes in Canada']

    crime_covid_canada_20_21 = plt.figure()

    covid_canada_20_21_axes = crime_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
    covid_canada_20_21_axes.plot(date_20_21, cases_20_21, label= 'Covid Cases')
    covid_canada_20_21_axes.plot(date_20_21, physical_20_21.iloc[0:20], label='Physical Crime Cases')
    covid_canada_20_21_axes.plot(date_20_21, non_physical_20_21.iloc[0:20], label=' Non Physical Crime Cases')
    covid_canada_20_21_axes.plot(date_20_21, public_axes_20_21.iloc[0:20], label='Public Crime Cases')
    covid_canada_20_21_axes.plot(date_20_21, private_axes_20_21.iloc[0:20], label='Private Crime Cases')

    # Formatting thr graph
    covid_canada_20_21_axes.set_title('Covid Cases and Crime Rate Overview')
    covid_canada_20_21_axes.set_xlabel('Month')
    covid_canada_20_21_axes.set_ylabel('Count')
    covid_canada_20_21_axes.legend()

    status = tk.Label(root, text="Graph Successfully Plotted", font=paragraph_font)
    status.grid(row=7, column=0, sticky="WE")

graph_button_1 = tk.Button(root, text="Graph It!", command = canada_covid_crime)
graph_button_1.grid(row=8,column=0)



# ------------------------------  Formatting + Necessary Code ----------------------------- #
root.mainloop()




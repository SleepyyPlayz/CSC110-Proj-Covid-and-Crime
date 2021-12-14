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



# Total Physical Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_physical_df['Date']
physical_crimes_20_21 = df.total_police_data_canada_20_21_physical_df['Total Physical Crimes in Canada']
# physical_crimes_canada_20_21 = plt.figure(1)
# physical_crimes_canada_20_21_axes = physical_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# physical_crimes_canada_20_21_axes.plot(date_20_21, physical_crimes_20_21)
covid_canada_20_21_axes.plot(date_20_21, physical_crimes_20_21)

# Total Non Physical Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_non_physical_df['Date']
non_physical_crimes_20_21 = \
     df.total_police_data_canada_20_21_non_physical_df['Total Non Physical Crimes in Canada']
# non_physical_crimes_canada_20_21 = plt.figure()
# non_physical_crimes_canada_20_21_axes = non_physical_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# non_physical_crimes_canada_20_21_axes.plot(date_20_21, non_physical_crimes_20_21)

# Total Public Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_public_df['Date']
public_crimes_20_21 = \
     df.total_police_data_canada_20_21_public_df['Total Public Crimes in Canada']
# public_crimes_canada_20_21 = plt.figure()
# public_crimes_canada_20_21_axes = public_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# public_crimes_canada_20_21_axes.plot(date_20_21, public_crimes_20_21)

# Total Private Crimes Graph for Canada for 2020 and 2021
# date_20_21 = df.total_police_data_canada_20_21_private_df['Date']
private_crimes_20_21 = \
     df.total_police_data_canada_20_21_private_df['Total Private Crimes in Canada']
# private_crimes_canada_20_21 = plt.figure()
# private_crimes_canada_20_21_axes = private_crimes_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
# private_crimes_canada_20_21_axes.plot(date_20_21, private_crimes_20_21)



# Graph name, x axes label, y axes label, wrapper, colour, legend
#------------------------------------------------------------------------------------#
# Covid Cases per Province Graph for Canada for 2020 and 2021

# ---------------------------- Tkinter Program -------------------------------------------------- #
root = tk.Tk()
root.title('Visualizing Covid Data')
root.geometry('600x600')

def canada_covid_crime(y_axes):
    title_variable = "Total Physical Crimes in Canada"

    if y_axes == "Physical" or y_axes == "physical":
        crime_axes = df.total_police_data_canada_20_21_physical_df['Total Physical Crimes in Canada']
    elif y_axes == "Non Physical" or y_axes == "non physical":
        crime_axes = \
            df.total_police_data_canada_20_21_non_physical_df['Total Non Physical Crimes in Canada']
    elif y_axes == "Public" or y_axes == "public":
        crime_axes = \
            df.total_police_data_canada_20_21_public_df['Total Public Crimes in Canada']
    elif y_axes == "Private" or y_axes == "private":
        crime_axes = \
            df.total_police_data_canada_20_21_private_df['Total Private Crimes in Canada']
    else:
        print("Please Enter a Valid Value")
    date_20_21 = df.covid_data_canada_20_21_df['Date']
    cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
    covid_canada_20_21 = plt.figure()
    covid_canada_20_21_axes = covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
    covid_canada_20_21_axes.plot(date_20_21, cases_20_21)
    covid_canada_20_21_axes.set_title('Covid Cases and ' + title_variable)

    covid_canada_20_21_axes.plot(date_20_21, crime_axes)

input_graph_type = tk.Entry(root, width=100, text="this is a text box")
input_graph_type.pack()
myB = tk.Button(text="Click to Graph", command = lambda: canada_covid_crime(input_graph_type.get()))
myB.pack()


# ------------------------------  Formatting + Necessary Code ----------------------------- #
root.mainloop()

# ------------------------------------- MAIN RUNNING SECTION --------------------------------- #
if __name__ == '__main__':
    from pprint import pprint
    #print(physical_crimes_2020)
    #print(covid_canada_2021)




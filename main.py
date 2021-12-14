"""
Copyright and Usage Information
===============================

This file was created for a final project for the University of Toronto Computer Science Course CSC110.
Any reproduction of this code without permission from the authors is strictly prohibited.

This file is Copyright (c) 2021 Nicholas Poon, Raghav Srinivasan, Khushil Nagda, and Wangzheng Jiang.
"""
import tkinter as tk, dataframes as df
import matplotlib.pyplot as plt
import numpy as np


# ---------------------------- Tkinter Program -------------------------------------------------- #
root = tk.Tk()
root.title('Visualizing Covid Data')
root.geometry('900x500')
root.configure(background="#FFFFFF")

title_font = ("Arial", 16, "bold")
paragraph_font = ("Arial", 14, "italic")
button_font = ("Arial", 16, "bold")

frame_heading_1 = tk.Label(root, text = "Visualising the relationship between Total Covid Cases in Canada and "
                                                     "Crime Rates", font = title_font, bg= 'white')
frame_heading_1.grid(row=0, column=0, columnspan = "15", sticky = "W", ipadx=10, ipady=10)

def canada_covid_crime_line():
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

    # Formatting the graph
    covid_canada_20_21_axes.set_title('Covid Cases and Crime Rate Overview')
    covid_canada_20_21_axes.set_xlabel('Month')
    covid_canada_20_21_axes.set_ylabel('Count')
    covid_canada_20_21_axes.legend()

    status = tk.Label(root, text="Graph Successfully Plotted", font=paragraph_font, bg="white")
    status.grid(row=2, column=4, sticky="WE")

graph_button_1 = tk.Button(root, text="Covid Cases & Crime Rate against Time", command = canada_covid_crime_line, padx=10, pady=10, bg= "#47aeed", fg= "white",
                           font = button_font)
graph_button_1.grid(row=1, column=4, sticky="WE")


def physical_crime_scatter():
    cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']

    # ----------------- Total PHYSICAL Crimes in relation to COVID Analysis -------------------- #

    # Graph
    physical_covid_canada_20_21 = plt.figure()
    physical_covid_canada_20_21_axes = physical_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
    physical_crimes_20_21 = df.total_police_data_canada_20_21_physical_df['Total Physical Crimes in Canada']
    # date_20_21 = df.total_police_data_canada_20_21_physical_df['Date']
    physical_covid_canada_20_21_axes.scatter(cases_20_21, physical_crimes_20_21.iloc[0:20])

    # Stat Analysis and Regression Plot
    physical_model = np.polyfit(cases_20_21, physical_crimes_20_21.iloc[0:20], 1)
    physical_predict = np.poly1d(physical_model)
    x_lin_reg = range(cases_20_21.min(), cases_20_21.max())
    y_lin_reg = physical_predict(x_lin_reg)
    physical_covid_canada_20_21_axes.plot(x_lin_reg, y_lin_reg, c='r')

    physical_r = round(np.corrcoef(cases_20_21, physical_crimes_20_21.iloc[0:20])[0, 1], 7)

    # Formatting the graph
    physical_covid_canada_20_21_axes.set_title("Relationship between Covid Cases & Physical Crime Cases (r=" + str(physical_r) + ')')
    physical_covid_canada_20_21_axes.set_xlabel('Total Covid Cases Canada')
    physical_covid_canada_20_21_axes.set_ylabel('Total Physical Crime Cases Canada')
    physical_covid_canada_20_21_axes.legend()

    status = tk.Label(root, text="Graph Successfully Plotted", font=paragraph_font)
    status.grid(row=4, column=4, sticky="WE")

graph_button_2 = tk.Button(root, text="Covid Cases vs Physical Crime Cases", command=physical_crime_scatter, padx=10, pady=10,
                           bg="#cf7ce6", fg="white",
                           font=button_font)
graph_button_2.grid(row=3, column=4, sticky="WE")

def non_physical_crime_scatter():
    cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
    # Graph
    non_physical_covid_canada_20_21 = plt.figure()
    non_physical_covid_canada_20_21_axes = non_physical_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
    non_physical_crimes_20_21 = \
        df.total_police_data_canada_20_21_non_physical_df['Total Non Physical Crimes in Canada']
    non_physical_covid_canada_20_21_axes.scatter(cases_20_21, non_physical_crimes_20_21.iloc[0:20])

    # Stat Analysis and Regression Plot
    non_physical_model = np.polyfit(cases_20_21, non_physical_crimes_20_21.iloc[0:20], 1)
    non_physical_predict = np.poly1d(non_physical_model)
    x_lin_reg = range(cases_20_21.min(), cases_20_21.max())
    y_lin_reg = non_physical_predict(x_lin_reg)
    non_physical_covid_canada_20_21_axes.plot(x_lin_reg, y_lin_reg, c='r')

    non_physical_r = round(np.corrcoef(cases_20_21, non_physical_crimes_20_21.iloc[0:20])[0, 1], 7)

    # Formatting the graph
    non_physical_covid_canada_20_21_axes.set_title("Relationship between Covid Cases & Non Physical Crime Cases (r=" + str(non_physical_r) + ')')
    non_physical_covid_canada_20_21_axes.set_xlabel('Total Covid Cases Canada')
    non_physical_covid_canada_20_21_axes.set_ylabel('Total Non Physical Crime Cases Canada')
    non_physical_covid_canada_20_21_axes.legend()

    status = tk.Label(root, text="Graph Successfully Plotted", font=paragraph_font, bg= 'white')
    status.grid(row=6, column=4, sticky="WE")

graph_button_3 = tk.Button(root, text="Covid Cases vs Non Physical Crime Cases", command=non_physical_crime_scatter,
                           padx=10, pady=10, bg="#84cc6c", fg="white", font=button_font)
graph_button_3.grid(row=5, column=4, sticky="WE")


def public_crime_scatter():
    cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
    # Graph
    public_covid_canada_20_21 = plt.figure()
    public_covid_canada_20_21_axes = public_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
    public_crimes_20_21 = \
        df.total_police_data_canada_20_21_public_df['Total Public Crimes in Canada']
    public_covid_canada_20_21_axes.scatter(cases_20_21, public_crimes_20_21.iloc[0:20])

    # Stat Analysis and Regression Plot
    public_model = np.polyfit(cases_20_21, public_crimes_20_21.iloc[0:20], 1)
    public_predict = np.poly1d(public_model)
    x_lin_reg = range(cases_20_21.min(), cases_20_21.max())
    y_lin_reg = public_predict(x_lin_reg)
    public_covid_canada_20_21_axes.plot(x_lin_reg, y_lin_reg, c='r')

    public_r = round(np.corrcoef(cases_20_21, public_crimes_20_21.iloc[0:20])[0, 1], 7)

    # Formatting the graph
    public_covid_canada_20_21_axes.set_title("Relationship between Covid Cases & Public Crime Cases (r=" + str(public_r) + ')')
    public_covid_canada_20_21_axes.set_xlabel('Total Covid Cases Canada')
    public_covid_canada_20_21_axes.set_ylabel('Total Public Crime Cases Canada')
    public_covid_canada_20_21_axes.legend()

    status = tk.Label(root, text="Graph Successfully Plotted", font=paragraph_font)
    status.grid(row=8, column=4, sticky="WE")

graph_button_4 = tk.Button(root, text="Covid Cases vs Public Crime Cases", command=public_crime_scatter,
                           padx=10, pady=10, bg="#de9440", fg="white", font=button_font)
graph_button_4.grid(row=7, column=4, sticky="WE")


def private_crime_scatter():
    cases_20_21 = df.covid_data_canada_20_21_df['Number of New Active Cases in Canada']
    # Graph
    private_covid_canada_20_21 = plt.figure()
    private_covid_canada_20_21_axes = private_covid_canada_20_21.add_axes([0.1, 0.1, 0.8, 0.8])
    private_crimes_20_21 = \
        df.total_police_data_canada_20_21_private_df['Total Private Crimes in Canada']
    private_covid_canada_20_21_axes.scatter(cases_20_21, private_crimes_20_21.iloc[0:20])

    # Stat Analysis and Regression Plot
    private_model = np.polyfit(cases_20_21, private_crimes_20_21.iloc[0:20], 1)
    private_predict = np.poly1d(private_model)
    x_lin_reg = range(cases_20_21.min(), cases_20_21.max())
    y_lin_reg = private_predict(x_lin_reg)
    private_covid_canada_20_21_axes.plot(x_lin_reg, y_lin_reg, c='r')

    private_r = round(np.corrcoef(cases_20_21, private_crimes_20_21.iloc[0:20])[0, 1], 7)
    private_covid_canada_20_21_axes.set_title("Covid -> Total Private Crime (r=" + str(private_r) + ')')

    # Formatting the graph
    private_covid_canada_20_21_axes.set_title("Relationship between Covid Cases & Private Crime Cases (r=" + str(private_r) + ')')
    private_covid_canada_20_21_axes.set_xlabel('Total Covid Cases Canada')
    private_covid_canada_20_21_axes.set_ylabel('Total Private Crime Cases Canada')
    private_covid_canada_20_21_axes.legend()

    status = tk.Label(root, text="Graph Successfully Plotted", font=paragraph_font, bg= 'white')
    status.grid(row=10, column=4, sticky="WE")


graph_button_5 = tk.Button(root, text="Covid Cases vs Private Crime Cases", command=private_crime_scatter,
                           padx=10, pady=10, bg="#de5240", fg="white", font=button_font)
graph_button_5.grid(row=9, column=4, sticky="WE")
# ------------------------------  Formatting + Necessary Code ----------------------------- #
root.mainloop()




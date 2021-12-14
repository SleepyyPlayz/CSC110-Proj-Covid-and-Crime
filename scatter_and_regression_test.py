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
import numpy as np

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
physical_covid_canada_20_21_axes.set_title("Covid -> Total Physical Crime (r=" + str(physical_r) + ')')


# ------------------ Total NON PHYSICAL Crimes in relation to COVID Analysis ---------------- #

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
non_physical_covid_canada_20_21_axes.set_title("Covid -> Total Non-Physical Crime (r=" + str(non_physical_r) + ')')


# ------------------ Total PUBLIC Crimes in relation to COVID Analysis --------------------- #

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
public_covid_canada_20_21_axes.set_title("Covid -> Total Public Crime (r=" + str(public_r) + ')')


# ------------------ Total PRIVATE Crimes in relation to COVID Analysis -------------------- #

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

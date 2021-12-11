import matplotlib
import pandas
import statsmodels

import read_and_analyze as RNA

covid_data_raw = RNA.read_covid_data('data_sets/covid_data.csv')
police_data_raw = RNA.read_police_data('data_sets/police_data.csv')

covid_data_ontario_jan_2020 = RNA.get_covid_data(covid_data_raw, 'Ontario', 2020)
police_data_ontario_jan_2020 = RNA.get_crime()

if __name__ == '__main__':
    pass

import matplotlib
import pandas
import statsmodels

import read_and_analyze as RNA

covid_data_raw = RNA.read_covid_data('data_sets/covid_data.csv')
police_data_raw = RNA.read_police_data('data_sets/police_data.csv')

# Covid Data for Canada for 2020
covid_data_canada_2020 = RNA.get_covid_data(covid_data_raw, 'Canada', 2020)

# Covid Data for Each Province for 2020
for pt in RNA.PROV_AND_TERR:
    covid_data_2020 = RNA.get_covid_data(covid_data_raw, pt, 2020)

# Covid Data for Canada for 2021
covid_data_canada_2021 = RNA.get_covid_data(covid_data_raw, 'Canada', 2021)

# Covid Data for Each Province for 2021
for pt in RNA.PROV_AND_TERR:
    covid_data_2021 = RNA.get_covid_data(covid_data_raw, pt, 2021)

# Physical and Non Physical Crimes for Canada for 2020
police_data_canada_2020_physical, police_data_canada_2020_non_physical = RNA.get_police_data(police_data_raw, 'Canada',
                                                                                             2020, 'physical')

# Public and Private Crimes for Canada for 2020
police_data_canada_2020_public, police_data_canada_2020_private = RNA.get_police_data(police_data_raw, 'Canada', 2020,
                                                                                      'public')

# Physical and Non Physical Crimes for Canada for 2021
police_data_canada_2021_physical, police_data_canada_2021_non_physical = RNA.get_police_data(police_data_raw, 'Canada',
                                                                                             2021, 'physical')

# Public and Private Crimes for Canada for 2021
police_data_canada_2021_public, police_data_canada_2021_private = RNA.get_police_data(police_data_raw, 'Canada', 2021,
                                                                                      'public')

# Physical and Non Physical Crimes for Each Province for 2020
for pt in RNA.PROV_AND_TERR:
    police_data_2020_physical, police_data_2020_non_physical = RNA.get_police_data(police_data_raw, pt, 2020,
                                                                                   'physical')

# Public and Private Crimes for Each Province for 2020
for pt in RNA.PROV_AND_TERR:
    police_data_2020_public, police_data_2020_private = RNA.get_police_data(police_data_raw, pt, 2020, 'public')

# Physical and Non Physical Crimes for Each Province for 2021
for pt in RNA.PROV_AND_TERR:
    police_data_2021_physical, police_data_2021_non_physical = RNA.get_police_data(police_data_raw, pt, 2021,
                                                                                   'physical')

# Public and Private Crimes for Each Province for 2021
for pt in RNA.PROV_AND_TERR:
    police_data_2021_public, police_data_2021_private = RNA.get_police_data(police_data_raw, pt, 2021, 'public')

if __name__ == '__main__':
    pass

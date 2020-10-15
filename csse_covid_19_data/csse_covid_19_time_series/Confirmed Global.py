import datetime

import matplotlib.pyplot as plt
import pandas as pd

confirmed_global = pd.read_csv('time_series_covid19_confirmed_global.csv')
global_data_summed = confirmed_global.groupby('Country/Region').sum()
all_countries_confirmed = global_data_summed.drop(['Lat', 'Long'], axis=1).reset_index()

countries_to_plot = ['US', 'China', 'United Kingdom', 'Germany', 'Iraq']
start_date = '01/22/2020'
end_date = '10/13/2020'


def get_index_from_date(date_string):
    FIRST_DATE = datetime.datetime(2020, 1, 22)
    date_list = [int(x) for x in date_string.split('/')]
    date_object = datetime.datetime(date_list[-1], date_list[0], date_list[1])

    return (date_object - FIRST_DATE).days


dates = list(all_countries_confirmed)[1:]

start_index = get_index_from_date(start_date)
end_index = get_index_from_date(end_date)

x_values = dates[start_index:end_index]

for country in countries_to_plot:
    countries = all_countries_confirmed[all_countries_confirmed['Country/Region'] == country]
    y_values = [int(countries[col]) for col in x_values]
    plt.plot(x_values, y_values, label=country)

plt.title = 'Confirmed Cases Over Time'
skip = max(len(x_values) // 5, 1)
plt.xticks(x_values[::skip])
plt.xlabel("Date (MM/DD/YY)")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.show()

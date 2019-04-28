import numpy as np
import json
from matplotlib import pyplot as plt


# function to load, reformat and write to JSON format
def dataFormat(filename):
    '''
    load data to memory and reform to a dictionary, keyed by year. Save this
    dictionary to a json file
    '''
    with open(filename) as csvfile:
        content = np.genfromtxt(csvfile, delimiter=',', skip_header=1)

    rainfall_dict = {}
    year_list = list(map(int, set(content[:, 0])))

    for year in year_list:
        nested_list = []
        for row in content:
            if row[0] == year:
                nested_list.append(row[2])
        rainfall_dict[str(year)] = nested_list

    with open('rainfall_dict.json', 'w') as file:
        json.dump(rainfall_dict, file)


def plot_rainfall(json_file, year, colour='b'):
    '''
    plot rainfall for a given year. Default colour is blue
    '''
    rainfall_dict = json.load(open(json_file))
    y = rainfall_dict[str(year)]

    fig = plt.figure()
    plt.plot(y, colour)
    plt.title(f'Annual rainfall in {year}')
    plt.xlabel('day')
    plt.ylabel('rainfall')

    return fig


def plot_mean_rainfall(json_file, start_year, end_year):
    '''
    plot mean annual average over a given range
    '''
    rainfall_dict = json.load(open(json_file))

    year = start_year
    mean_rainfall = np.zeros(end_year - start_year + 1)
    while year <= end_year:
        mean_rainfall[year-start_year] = np.mean(rainfall_dict[str(year)])
        year += 1

    fig = plt.figure()
    plt.plot(np.linspace(start_year, end_year, (end_year - start_year + 1)),
             mean_rainfall)
    plt.title(f'mean annual rainfall between {start_year} and {end_year}')
    plt.xlabel('year')
    plt.ylabel('mean rainfall')

    return fig


def correct_value(rainfall_value):

    corrected_rainfall = (rainfall_value * 1.2) ** np.sqrt(2)

    return corrected_rainfall


def correct_rainfall_1(json_file, year):
    '''
    solved using a for loop
    pros: readable, easy to understand
    cons: lengthy code
    '''
    rainfall_dict = json.load(open(json_file))
    rainfall_year = rainfall_dict[str(year)]

    rainfall_corrected = np.zeros(len(rainfall_year))
    day = 0
    for rainfall_measured in rainfall_year:
        rainfall_corrected[day] = correct_value(rainfall_measured)
        day += 1

    return rainfall_corrected


def correct_rainfall_2(json_file, year):
    '''
    solved using list comprehension
    pros: consise
    cons: harder to understand
    '''
    rainfall_dict = json.load(open(json_file))
    rainfall_year = rainfall_dict[str(year)]

    rainfall_corrected = [correct_value(rainfall_measured) for
                          rainfall_measured in rainfall_year]

    return rainfall_corrected


filename = 'python_language_1_data.csv'
dataFormat(filename)


fig = plot_rainfall('rainfall_dict.json', 1998)
plt.savefig('rainfall_1998.png')

fig = plot_mean_rainfall('rainfall_dict.json', 1988, 2000)
plt.savefig('mean_rainfall_1988_2000.png')

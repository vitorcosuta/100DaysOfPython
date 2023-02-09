# Reading CSV (Comma Separated Values) files

# METHOD 1 - Very difficult to work with

# with open('weather_data.csv', mode='r') as data_file:
#     data = data_file.readlines()
#     print(data)  # --> ['day,temp,condition\n', 'Monday,12,Sunny\n', ...]


# METHOD 2 - A lot of faff involved just to read a simple column

# import csv
#
# with open('weather_data.csv', mode='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#
# print(temperatures)


# METHOD 3 - The most optimal method using Pandas library
import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))  # --> DataFrame
# print(type(data['temp']))  # --> Series

# Converting a DataFrame to a Dictionary
data_dict = data.to_dict()
# print(data_dict)

# Converting a Series to a List
temp_list = data['temp'].to_list()
# print(temp_list)

# round() function documentation: https://www.w3schools.com/python/ref_func_round.asp

# pandas.Series.mean() method documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean
average_temp = round(data['temp'].mean(), 1)
print(f'The average temperature of the week is {average_temp}°C.')

# pandas.Series.max() method documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max
max_temp = data['temp'].max()
print(f'The maximum temperature of the week is {max_temp}ºC.')


# Get data in columns
# print(data['condition'])
# print(data.condition)

# Get data in rows
# print(data[data.day == 'Monday'])
# print(data[data['day'] == 'Monday'])


# We can convert Series type to strings by using the panda.Series.to_string().
# We actually need to inform the parameter index=False in order to get rid of the indexes when printing the Series out.
# https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html#pandas.Series.to_string
hottest_day = data[data.temp == max_temp].day.to_string(index=False)
print(f'The hottest day of the week is {hottest_day}')


# Creating DataFrame from scratch
data_dict = {
    'students': ['Gabriel', 'Bianca', 'Jessie'],
    'scores': [78, 89, 55]
}

data = pandas.DataFrame(data_dict)
data.to_csv('students_data.csv')

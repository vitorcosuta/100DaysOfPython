import pandas

squirrel_data = pandas.read_csv('squirrel_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
black_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])

squirrel_count_dict = {
    'Fur Color': ['Black', 'Gray', 'Cinnamon'],
    'Count': [black_squirrels_count, gray_squirrels_count, cinnamon_squirrels_count]
}

count_data = pandas.DataFrame(squirrel_count_dict)
count_data.to_csv('squirrel_data/count_data.csv')
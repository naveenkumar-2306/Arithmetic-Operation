# intialize dictionary with default values

employees = ['Kelly', 'Emma']
default = {"designation":'Developer', "salary":8000}

my_dict = { employee : default for employee in employees }

print(my_dict)



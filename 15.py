#Initialize dictionary with default values
#employees = ['Kelly', 'Emma']
#defaults = {"designation": 'Developer', "salary": 8000}
#O/p: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

list_1 = []
dict_1 = {}
entry=int(input("Enter the number of entries:"))
for i in range(entry):
   key=input("Enter a key:")
   value=input("Enter the value:")
   dict_1[key]=value

n = int(input("Enter the number of employees"))
for i in range(n):
    name = input("Enter the name of the employee")
    list_1.append(name)
    
dict_2 = {}
for i in range(n):
    dict_2[list_1[i]] = dict_1
print(dict_2)




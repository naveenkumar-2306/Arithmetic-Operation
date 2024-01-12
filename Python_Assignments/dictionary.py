
## dictionary


print("\n Question 1 \n")
dict = {}

keys = ['Ten','Twenty','Thirty']
values = [10,20,30]

for i in range(len(keys)):
    dict[keys[i]] = values[i]


print("Dictionary Created :: ",dict)


##initialize the dictionary with default values

print("\n Question 2 \n")


employees = ['kelly','Emma']
defaults = {"designation" : 'Developer', "Salary" : 8000}

dict_new = {}
for i in employees:
    dict_new[i] = defaults

print("Old dictionary key values",dict_new,'\n')

dict_new['kelly']["designation"] = "Designer"  ## changed to Designer

print("New dictionary key values",dict_new)

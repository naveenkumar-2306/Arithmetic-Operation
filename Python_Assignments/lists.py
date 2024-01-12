import math

def list_the_same(my_list):

    if(list[0] == list[-1]):
        print("First and last are same")
    else:
        print("List are not same")


list = []
string_entered = input("Enter the list of values :: ")
list = string_entered.split()
list_the_same(list)




odd_list = input("Enter the list1 value only odd numbers :: ")
odd_list = odd_list.split()
even_list = input("Enter the list2 value only even numbers :: ")
even_list = even_list.split()
new_list = []
for i in odd_list:
    new_list.append(i)
for j in even_list:
    new_list.append(j)
print("new list",new_list)
print("odd list",odd_list)
print("even list",even_list)



input_integer = int(input("Enter the integer to extract each digit in reverse order :: "))
int_to_string = str(input_integer)
length=len(int_to_string)
initial_value = 1
temp = 0
num = []
while(input_integer != 0):
    num.append((input_integer % 10))
    input_integer = input_integer/10
    input_integer = math.trunc(input_integer)

num = num[::-1]

print(num)


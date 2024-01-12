
## Question 1 
print("\nQuestion 1 ")

tuple_var = ()

list_var = []

number = int(input("Enter the number of tuple values need to enter::"))
for i in range(number):
    integer = int(input("Enter the values one by one :: ")) ## 1 2 3 4 
    list_var.append(integer)



tuple_var = tuple(list_var)

tuple_var = tuple_var[::-1]   ## Tuple can change the value interchange the position,value change is not permitable

print("The reversed tuple values :: ",tuple_var)


print("\nQuestion 2\n ")

tuple_var = ()
tuple_var = (10,20,30,40) 
if(20 in tuple_var):
    print("yes")
    for i in tuple_var:
        if(i == 20):
            print(i)
else:
    print("no")


print("\nQuestion 3\n ")


tuple_var = (('d',44),('c',25),('b',9),('a',52)) ## Tuples cannot permit direct sort it is immutable

sorted_list = tuple(sorted(tuple_var, key=lambda x:x[1]))

print(sorted_list)


print("\nQuestion 4 \n")

tuple1 = (50,10,60,70,50)
print("\nThe total count of tuple ",tuple1.count(50))






















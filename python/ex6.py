# check if the first and last number of the list is the same

list=[]

n = int(input('enter the number of elements in the list:'))
for i in range(n):
    num = int(input("enter the element:"))
    list.append(num)

if list[0] == list[-1]:
    print (" it's the same ")
else:
    print("it's not the same")


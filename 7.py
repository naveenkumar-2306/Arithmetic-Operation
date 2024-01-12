#Create a new list from a two list using the following condition
#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

list_1=[]
list_2=[]

n1=int(input("Enter the number of elements in list1:"))
for i in range(0,n1):
  num1=int(input())
  list_1.append(num1)

n2=int(input("Enter the number of elements in list2:"))
for i in range(0,n2):
   num2=int(input())
   list_2.append(num2)
   
newlist=[]
for i in range(0,n1):
   if( list_1[i]%2 !=0):
      newlist.append(list_1[i])
      
for i in range(0,n2):
    if( list_2[i]%2 ==0):
      newlist.append(list_2[i])
      
print(newlist)

''' Create a new list from a two list using the following condition
→ Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
'''

list1 = []
list2 = []
new_list = []

n1=int(input("Enter the number of elements in list1:"))
for i in range(n1):
  num=int(input('enter the element:'))
  list1.append(num)

n2=int(input("Enter the number of elements in list2:"))
for i in range(n2):
   num=int(input('enter the element:'))
   list2.append(num)
   
for element in list1:
	if element % 2 != 0 :
		new_list.append(element)
		
for element in list2:
	if element % 2 == 0 :
		new_list.append(element)
		
print(new_list)
		

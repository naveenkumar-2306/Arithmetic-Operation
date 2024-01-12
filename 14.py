#Convert two lists into a dictionary
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

lists_1=[]
lists_2=[]

n1=int(input("Enter the number of elements in list1:"))
for i in range(0,n1):
  num1=input()
  lists_1.append(num1)

n2=int(input("Enter the number of elements in list2:"))
for i in range(0,n2):
   num2=input()
   lists_2.append(num2)
   
my_dict=dict(zip(lists_1,lists_2))
print(my_dict)

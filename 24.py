#Count the repeated number in the tuple

from collections import Counter
list_1=[]
num=int(input("Enter the number of elements in tuple:"))
for i in range(0,num):
   x=int(input())
   list_1.append(x)

tuple_1=tuple(list_1)
ele_count=Counter(tuple_1)
rep_ele_count={ele: count for ele,count in ele_count.items() if count>1}
for element,count in  rep_ele_count.items():
   print(f"{element}:{count} times")

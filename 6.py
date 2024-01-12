#Check if the first and last number of a list is the same


lists=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
  num=int(input())
  lists.append(num)

if lists[0] == lists[n-1]:
  print("First and last number of the list is same")
else:
  print("First and last number of the list is not same")




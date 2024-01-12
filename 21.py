#Reverse the tuple
tuple1=()
num=int(input("Enter the number of elements :"))
l = list(tuple1)
for i in range(0,num):
  var =int(input())
  l.append(var)

l=l[::-1]
tuple1=tuple(l)
print(tuple1)


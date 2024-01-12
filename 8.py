#Write a Program to extract each digit from an integer in the reverse order.

num=int(input("Enter an integer:"))
lists=[]
while num>0:
  digit=num%10
  lists.append(digit)
  num=num//10;
  
print(lists)

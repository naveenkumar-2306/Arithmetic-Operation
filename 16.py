
#Check if a value exists in a dictionary

user_dict= {}
num=int(input("Enter the number of key-value pairs you want:"))
for i in range(num):
  key=input("Enter a key:")
  value=input(f"Enter a value for {key}:")
  user_dict[key]=value
  
num2=input("Enter the value:")

if num2 in user_dict.values():
   print(f"{num2} exists in the dictionary")
else:
    print(f"{num2} doesnot exists in the dictionary")


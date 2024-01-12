employ_data={}
num_emp=int(input("Enter the number of emp:"))
for i in range(num_emp):
   emp_name=input("Enter emp name:")
   emp_info={}
   desig=input("Designation:")
   sal=int(input("salary:"))
   emp_info['desig']=desig
   emp_info['sal']=sal
   employ_data[emp_name]=emp_info
   
print(employ_data)

new_emp=input("Enter the employee name:")
new_key=input("Enter the key to change:")
new_value=input("Enter the value:")

if emp_name in employ_data:
  if new_key in employ_data[new_emp]:
      employ_data[new_emp][new_key]=new_value
      print("Updated dictionary")
      print(employ_data)
  else:
      print(f"The key '{new_key}' does not exist for employee '{emp_name}'.")
else:
  print(f"The employee '{emp_name}' does not exist in the dictionary")
  

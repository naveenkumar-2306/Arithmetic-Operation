from matplotlib import pyplot as plt
import numpy as np
from numpy import random


## question 1
month = np.array(0)
profit = np.array(0)
number_of_month = int(input("Enter how many month profit need to enter :: "))
for i in range(number_of_month):
    month_number = int(input("Enter the month number ::"))
    month = np.append(month,month_number)
    profit_number = int(input("Enter the profit of month {}::".format(month_number)))
    profit = np.append(profit,profit_number)
    
print(month)
print(profit) 

fig1 = plt.figure("Months and Profit Graph")
plt.subplot(1,2,1)
plt.plot(month,profit,'*-',color='r')
plt.xlabel("Month_Number",color = 'g')
plt.ylabel("Total Profit",color = 'b')
plt.title("Company Profit per month")

plt.subplot(1,2,2)
plt.stem(month,profit,'*')
plt.plot(month,profit,'*-',color='r')
plt.xlabel("Month_Number",color = 'g')
plt.ylabel("Total Profit",color = 'b')
plt.title("Company Profit per month")
plt.show()


##Question 2

month = np.arange(1,13)

face_cream = random.randint(1000,size=(12))

face_wash = random.randint(500,size=(12))

tooth_paste = random.randint(1500,size=(12))

tooth_brush = random.randint(2000,size=(12))

fig1 = plt.figure("Months and multiple products ")

plt.plot(month,face_cream,'*-',label = "Face-Cream",color='r',linewidth = 2)

plt.plot(month,face_wash,'--',color='g',label = "Face-wash",linewidth = 2)

plt.plot(month,tooth_paste,'-.',color='b',label = "tooth-paste",linewidth = 2)


plt.plot(month,tooth_brush,'-',color='k',label = "tooth-brush",linewidth = 2)

plt.plot()

##Question 3

fig1 = plt.figure("Subplots")

plt.subplot(2,1,1)
plt.plot(month,face_cream,'*-',color = 'r')
plt.xlabel("Month_Number",color = 'g')
plt.ylabel("Total Profit",color = 'b')
plt.title("Sales of Face_cream")

plt.subplot(2,1,2)
plt.plot(month,face_wash,'*-',color = 'k')
plt.xlabel("Month_Number",color = 'g')
plt.ylabel("Total Profit",color = 'b')
plt.title("Face_Wash")
plt.show()

##Question 4

month = np.arange(1,13)
print(month)
face_cream = random.randint(1000,size=(12))

fig1 = plt.figure("Bar Graph")

plt.bar(month,face_cream,label = "Face-Cream",color='b',width = 0.5)
plt.xlabel("Month_Number",color = 'g')
plt.ylabel("Total Profit",color = 'b')
plt.title("Bar graph profit per month")
plt.grid()
plt.show()



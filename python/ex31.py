'''
Read Total profit of all months and show it using a line plot
Total profit data provided for each month. Generated line plot must include the following properties: –
X label name = Month Number
Y label name = Total profit

'''
import matplotlib.pyplot as plt


num=[1,2,3,4,5,6,7,8,9,10]
profit=[210000,190000,210000,300000,215000,215000,212000,200000,300000,390000]

plt.plot(num, profit)

plt.title("Company profit per month")
plt.xlabel("Month number")
plt.ylabel("Total profit")

plt.show()


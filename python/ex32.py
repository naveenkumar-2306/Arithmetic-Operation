'''
Display the number of units sold per month for each product using multi line plots. (i.e., Separate Plotline for each product ).
'''

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]

y1 = [10000, 6000,10000,9000,7000,8500]
y2 = [5000, 4500,4000,6000,4600,4500]
y3 = [2200, 2300, 2000, 2500, 3000, 2700]

plt.plot(x,y1, label = 'toothpaste sales data')
plt.plot(x,y2, label = 'face wash sales data')
plt.plot(x,y3, label = 'face cream sales data')

plt.title("sales data")
plt.xlabel("Month number")
plt.ylabel("sales unit in number")


plt.show()


# Read sales data of bathing soap of all months and show it using a bar chart

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]

y1 = [10000, 6000,10000,9000,7000,8500]

plt.bar(x,y1, color ='blue', width = 0.4)

plt.xlabel("Month number")
plt.ylabel("sales units")
plt.title("bathingsoap sales data")

plt.show()

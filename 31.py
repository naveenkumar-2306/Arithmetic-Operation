#Read Total profit of all months and show it using a line plot

import matplotlib.pyplot as plt
import numpy as np

Month_num=[1,2,3,4,5,6,7,8,9,10,11,12]
Total_profit=np.array([100000,100000,200000,300000,400000,500000,600000,700000,800000,900000,100000,200000])
plt.plot(Month_num, Total_profit)
plt.title("Company profit per month")
plt.xlabel("Month number")
plt.ylabel("Total profit")
plt.show()

#Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=np.array([2,4,6,8,10,12,14,16,18,20,22,24])

plt.bar(x,y,width=0.9,color="blue")
plt.title("Bathingsoap sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.show()


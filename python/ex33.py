# Read Bathing soap facewash of all months and display it using the Subplot

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]

y1 = [10000, 6000,10000,9000,7000,8500]
y2 = [5000, 4500,4000,6000,4600,4500]

fig,ax = plt.subplots(nrows = 2, ncols = 1)
ax[0].plot(x,y1)
ax[1].plot(x,y2)

ax[0].set_title('sales of bathing soap')
ax[1].set_title('sales of facewash')

ax[0].set_ylabel('sales units')
ax[0].set_xlabel('month number')

ax[1].set_ylabel('sales units')
ax[1].set_xlabel('month number')


plt.show()

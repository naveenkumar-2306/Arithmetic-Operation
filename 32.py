#Read all product sales data and show it  using a multi line plot

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]
x3 = [1, 2, 3, 4, 5]
y3 = [5, 4, 3, 2, 1]

x4 = [2,4,6,3,8]
y4 = [4,7,5,9,2]

x5 = [5,6,2,1,8]
y5 = [7,8,9,4,2]

x6= [3,7,4,6,5]
y6= [3,4,1,7,6]
plt.plot(x1, y1, label='Face Cream Sales Data')
plt.plot(x2, y2, label='Face Wash Sales Data')
plt.plot(x3, y3, label='ToothPaste Sales Data')
plt.plot(x4, y4, label='ToothPaste Sales Data')
plt.plot(x5, y5, label='ToothPaste Sales Data')
plt.plot(x6, y6, label='ToothPaste Sales Data')
plt.legend()
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.show()

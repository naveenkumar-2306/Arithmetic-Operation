import matplotlib.pyplot as plt
import numpy as np
mon_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
p1_ls = [10,17,13,19,32,23,55,47,19,98,103,121]
p2_ls = [13,34,65,23,77,44,22,33,55,21,42,24]
p3_ls = [32,44,12,66,77,44,56,78,23,99,43,22]
p4_ls = [45,70,10,54,45,65,33,87,33,65,22,77]
plt.subplot(2,3,1)
plt.plot(mon_ls,p1_ls,marker='o')
plt.title("Product 1 sales")
plt.xlabel("Month number")
plt.ylabel("total profit in thousands")
plt.subplot(2,3,3)
plt.plot(mon_ls,p2_ls,maker='o')
plt.title("Product 2 sales")
plt.xlabel("Month number")
plt.ylabel("total profit in thousands")
plt.suptitle("Company profi per month")
plt.show()

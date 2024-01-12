import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
mon_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
p1_ls = [10,17,13,19,32,23,55,47,19,98,103,121]
plt.bar(mon_ls,p1_ls)
plt.title("Product 1 sales")
plt.grid()
plt.xlabel("Month number")
plt.ylabel("total profit in thousands")
plt.savefig("py_mstplot_q33.jpg")
plt.show()


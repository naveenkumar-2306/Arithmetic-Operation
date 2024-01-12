import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
mon_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
p1_ls = [10,17,13,19,32,23,55,47,19,98,103,121]
p2_ls = [13,34,65,23,77,44,22,33,55,21,42,24]
p3_ls = [32,44,12,66,77,44,56,78,23,99,43,22]
p4_ls = [45,70,10,54,45,65,33,87,33,65,22,77]
data = {"product 1":p1_ls,"product 2":p2_ls,"product 3":p3_ls,"product 4":p4_ls}
df = pd.DataFrame(data)
df.plot(marker = 'o')
plt.xlabel("Month number")
plt.ylabel("total profit in thousands")
plt.title("Company profi per month")
plt.show()

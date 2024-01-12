import matplotlib.pyplot as plt
import numpy as np
mon_ls = [1,2,3,4,5,6,7,8,9,10,11,12]
profit_ls = [110,117,103,109,117,102,110,104,109,98,103,121]
x1 = np.array(mon_ls)
y1 = np.array(profit_ls)
fig, x = plt.subplots()
x.plot(x1,y1)
plt.xlabel("Month number")
plt.ylabel("total profit in thousands")
x.set_xticks(np.arange(1,13,1))
plt.title("Company profi per month")
plt.show()

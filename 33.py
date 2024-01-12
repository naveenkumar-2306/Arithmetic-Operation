#Read Bathing soap facewash of all months and display it using the Subplot

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([2, 4, 6, 7, 9, 1, 4, 5, 7, 6, 4, 3])
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

y2 = np.array([3, 4, 6, 8, 2, 4, 5, 8, 5, 2, 8, 9])
x2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

fig, (sub1, sub2) = plt.subplots(2,1) 

sub1.plot(x1, y1,color="green")  
sub2.plot(x2, y2,color="red") 

sub1.set_title("Sales data of a bathing soap")
sub2.set_title("Sales data of a facewash")

sub2.set_xlabel("Month Number") 
sub2.set_ylabel("Sales units in number")
sub1.set_xticks(np.arange(1, 13, 1))
sub2.set_xticks(np.arange(1, 13, 1))
sub1.set_yticks(np.arange(1,10,1))
sub2.set_yticks(np.arange(1,10,1))
plt.show()



# create a 5X2 int array from range (100, 200) such that the difference between each element is 10.

import numpy

a = numpy.arange(100,200,10)
print(a.reshape(5,2))

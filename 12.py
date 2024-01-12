#Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
import numpy

print("5x2 array from range between 100 to 200 that the difference between each element is 10")
sampleArray = numpy.arange(100, 200, 10)
sampleArray = sampleArray.reshape(5,2)
print (sampleArray)

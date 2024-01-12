#Recursive function to calculate sum of numbers from 0 to 10

def calc_sum(n):
 if (n==0):
    return 0
 else:
    return n + calc_sum(n-1)
    
result=calc_sum(10)
print(result)


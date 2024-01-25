# create recursive function

n = int(input('enter n:'))

def printing (num):
	if(num == 0):
		return
	else:
		print(num)
		printing(num-1)

printing(n)

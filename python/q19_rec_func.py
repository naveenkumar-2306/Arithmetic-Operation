#recursive function for performing addition of first n numbers
def recfunc(num):
	if num == 1:
		return 1
	else:
		return num + recfunc(num-1)
		
n = int(input("Enter a number"))
su = recfunc(n)
print(f"The sum is: {su}")

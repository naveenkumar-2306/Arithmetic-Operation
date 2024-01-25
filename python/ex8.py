# extract each digit from an integer in reverse order

number = int(input("enter a number: "))

reverse = 0

while number > 0:
	last_digit = number % 10
	reverse = (reverse *10) + last_digit
	number = number //10
	
print (reverse)

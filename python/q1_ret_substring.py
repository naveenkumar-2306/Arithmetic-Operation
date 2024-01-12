#Return the count of a given substring from a string
inp_str = input("Please enter the string")
sub_str = input("Please enter the substring")
count = inp_str.count(sub_str)
print(f"the substring: <{sub_str}> has occured {count} times in the string <inp_str>.")

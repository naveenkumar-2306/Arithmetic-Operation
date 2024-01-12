#Replace a substring with new substring.  Ex: “image.png” replace ‘.png’ with ‘.jpg’
fullstring=input("Enter a string:")
substring=input("Enter the string to get replaced:")
substring2=input("Enter the filler string:")
new_string=fullstring.replace(substring,substring2)
print(new_string)

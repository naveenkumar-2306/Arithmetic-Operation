'''

Return the count of given substring from a string

'''

def string_count(my_str):
    count = 0
    index = 0
    index_limit = len(my_str)
    split_str = my_str.split()
    for i in range(len(split_str)):
        for string_count,item in enumerate(split_str[i]):
            item = item
            string_count =string_count + 1
        print(f'item {split_str[i]} value {string_count}')

def string_even_index(my_str):
    len_of_string = len(my_str)
    for i in range(len_of_string):
        if(i%2 == 0):
            print(my_str[i])

def split_on_spaces(my_str):
    split_str = my_str.split()
    print(split_str)

def string_reverse(my_str):
   strrev = my_str[::-1]
   print(strrev)

def str_replace(my_str,string_find,string_replace):
    replace_str = my_str.replace(string_find,string_replace)
    print(replace_str)
  ##  replace_str_length = len(string_replace)



my_str = input("Enter the string want to alter ::")

## 1. Return the count of a given substring from a string

##string_count(my_str)

## 2. Print characters from a string that are present at an even index number.

##string_even_index(my_str)

## 3. Split a string on spaces.

##split_on_spaces(my_str)

## 4. Reverse a given string.

##string_reverse(my_str)

## 5. Replace a substring with new substring.  Ex: “image.png” replace ‘.png’ with ‘.jpg’


str_replace(my_str,"image.png",".png")

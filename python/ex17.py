# change value of a key in nested dictionary

n1 = int(input('enter the number of elements in dictionary: '))
n2 = int(input('enter the number of elements in nested dictionary: '))

dic = {}
sub_dic = {}

for i in range (n1):
	key1 = input('enter the key for diciontary:')
	for j in range (n2):
		key2 = input('enter the key for nested diciontary:')
		value = input('enter the value:')
		sub_dic[key2] = value
	dic[key1] = sub_dic
	
print(dic)

key1 = input('enter the key for which the value needs to be changed:')
key2 = input('enter the nested key for which the value needs to be changed:')

value = input('enter the value:')

dic[key1][key2] = value

print(dic)

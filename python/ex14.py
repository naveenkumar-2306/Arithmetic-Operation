# convert two list into dictionary

keys = ['ten', 'tewnty','thirty']

values = [10,20,30]

res_dict = { keys[i] : values[i] for i in range (len(keys)) }

print (res_dict)

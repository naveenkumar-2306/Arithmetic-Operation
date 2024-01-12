#Sort a tuple of tuples by 2nd item
#Ex: Tuple1 = ((‘a’,44),(‘b’,25),(‘c’,9),(‘d’,52))

Tuple1 = (('a',44),('b',25),('c',9),('d',52))
Tuple1=tuple(sorted(list(Tuple1),key=lambda a: a[1]))
print(Tuple1)


my_set = {'a', 'b', 'c', 'd'} #set
my_set.add('c') #add
my_set.add('e')
for i in my_set:
	print(i)
my_set.remove('b') #delete
print('b' in my_set)
my_set.update({1, 2, 3})
for i in my_set:
	print(i)

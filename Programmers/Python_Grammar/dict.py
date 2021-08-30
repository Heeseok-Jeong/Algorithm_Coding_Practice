my_dict = {'a' : 1, "c" : 3, "b" : 2}
print(my_dict)

my_dict[5] = 'e'
print(my_dict)

del my_dict[5]
print(my_dict)

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

print(my_dict.get('b'))

print(2 in my_dict)
print('a' in my_dict)

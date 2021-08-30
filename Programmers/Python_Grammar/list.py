def show_list():
    for i in my_list:
        print(i, end=' ')
    print()

my_list = [1, 2, 3, ['a', 'b']]
my_list.append(10)
show_list()

del my_list[0]
show_list()

my_list.remove(3)
show_list()

# my_list.sort()
# show_list()

my_list.reverse()
show_list()

my_list.insert(1, 'k')
show_list()

my_list.pop()
show_list()

my_list.extend([5, 15, 25])
show_list()

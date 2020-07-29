import sys

def get_possible_num(x, y):
    possible_list = [i for i in range(1, size+1)]

    for i in range(size):
        #row
        if n_list[x][i] in possible_list:
            possible_list.remove(n_list[x][i])
        #col
        if n_list[i][y] in possible_list:
            possible_list.remove(n_list[i][y])

    #lec
    new_x = (x//3)*3
    new_y = (y//3)*3
    for i in range(new_x, new_x+3):
        for j in range(new_y, new_y+3):
            if n_list[i][j] in possible_list:
                possible_list.remove(n_list[i][j])

    return possible_list

def solve(zero_index):
    global done

    if done:
        return

    if zero_index == len(zero_point):
        done = True
        for row in n_list:
            print(*row)
        return

    x, y = zero_point[zero_index]
    possible_list = get_possible_num(x, y)
    # print(x, y, ":", possible_list)
    # print()

    for num in possible_list:
        n_list[x][y] = num
        solve(zero_index+1)
        n_list[x][y] = 0

size = 9
n_list = [list(map(int, sys.stdin.readline().split())) for i in range(size)]
zero_point = [[i, j] for i in range(size) for j in range(size) if n_list[i][j] == 0]
zero_index = 0
done = False
# print()
solve(zero_index)

from copy import deepcopy

def check_sinking(world, i, j):
    wr = [-1, 0, 1, 0]
    wc = [0, 1, 0, -1]

    count = 0
    for k in range(4):
        if world[i+wr[k]][j+wc[k]] == '.':
            count += 1

    if count >= 3:
        return True
    return False

def get_compressed_location(new_world, R, C):
    N, E, S, W = R+1, 0, 0, C+1
    for i in range(R+2):
        for j in range(C+2):
            if new_world[i][j] == 'X':
                if N > i:
                    N = i
                if S < i:
                    S = i
                if W > j:
                    W = j
                if E < j:
                    E = j

    return N, S, W, E


R, C = map(int, input().split())
world = [['.' for _ in range(C+2)] for _ in range(R+2)]
for i in range(R):
    original = input()
    for j in range(len(original)):
        type = original[j]
        
        world[i+1][j+1] = type

new_world = deepcopy(world)
for i in range(R+2):
    for j in range(C+2):
        if world[i][j] == 'X' and check_sinking(world, i, j):
            new_world[i][j] = '.'

N, S, W, E = get_compressed_location(new_world, R, C)

for i in range(N, S+1):
    for j in range(W, E+1):
        print(new_world[i][j], end='')
    print()

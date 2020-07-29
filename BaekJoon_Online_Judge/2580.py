import sys

size = 9

def read_sys():
    return sys.stdin.readline()

def get_input(arr_sudoku):
    for i in range(size):
        arr_sudoku.append(list(map(int, read_sys().split())))

def check_zero_location(arr_sudoku, arr_zero_location):
    for i in range(size):
        for j in range(size):
            if arr_sudoku[i][j] == 0:
                arr_zero_location.append((i, j))

def solve_sudoku2(arr_sudoku, arr_zero_location):
    for i, j in arr_zero_location:
        return

def solve_sudoku(arr_sudoku, arr_zero_location):
    for i, j in arr_zero_location:
        visited = [False] * (size+1)
        count = 0
        zero_location = []
        # check row
        for row in arr_sudoku[i]:
            if row != 0 and visited[row] == False:
                visited[row] = True
        for k in range(1, size+1):
            if visited[k] == False:
                zero_location.append(k)
                count += 1
        if count == 1:
            arr_sudoku[i][j] = zero_location.pop()
            continue
        # check col
        for row in range(size):
            col =  arr_sudoku[row][j]
            if col != 0 and visited[col] == False:
                print(col)
                visited[col] = True
                print(visited)
        for k in range(1, size+1):
            if visited[k] == False:
                zero_location.append(k)
                count += 1
        if count == 2:
            arr_sudoku[i][j] = zero_location.pop()
            continue
        # check sector
        # if i<3:
        #     if j<3:
        #         a=0
        #     elif j<6:
        #         a=1
        #     else:
        #         a=2
        # elif i<6:
        #     if j<3:
        #         a=0
        #     elif j<6:
        #         a=1
        #     else:
        #         a=2
        # else:
        #     if j<3:
        #         a=0
        #     elif j<6:
        #         a=1
        #     else:
        #         a=2
        #
        # for row in range(size):
        #     col =  arr_sudoku[row][j]
        #     if col != 0 and visited[col] == False:
        #         print(col)
        #         visited[col] = True
        #         print(visited)
        # for k in range(1, size+1):
        #     if visited[k] == False:
        #         zero_location.append(k)
        #         count += 1
        # if count == 2:
        #     arr_sudoku[i][j] = zero_location.pop()
        #     continue


def print_result(arr_sudoku):
    for i in arr_sudoku:
        result = ""
        for j in i:
            result += str(j)
            result += " "
        print(result)

arr_sudoku = []
arr_zero_location = []
get_input(arr_sudoku)
# print(arr_sudoku)
check_zero_location(arr_sudoku, arr_zero_location)
solve_sudoku(arr_sudoku, arr_zero_location)
print()
print_result(arr_sudoku)

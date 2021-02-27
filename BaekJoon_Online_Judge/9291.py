def check_row(sudoku):
    result = True
    for i in range(9):
        check_list = [False for _ in range(10)]
        for j in range(9):
            # print(f"i : {i}, j : {j}, sudoku[i][j] : {sudoku[i][j]}")
            if check_list[sudoku[i][j]] == True:
                result = False
                break
            else:
                check_list[sudoku[i][j]] = True
        # print(result)
        if result == False:
            break
    # print("row :", result)
    return result

def check_col(sudoku):
    result = True
    for i in range(9):
        check_list = [False for _ in range(10)]
        for j in range(9):
            # print(f"i : {i}, j : {j}, sudoku[i][j] : {sudoku[i][j]}")
            if check_list[sudoku[j][i]] == True:
                result = False
                break
            else:
                check_list[sudoku[j][i]] = True
        # print(result)
        if result == False:
            break
    # print("col :", result)
    return result

def check_3by3(sudoku):
    result = True
    for i in range(3):
        for j in range(3):
            check_list = [False for _ in range(10)]
            for k in range(3):
                for l in range(3):
                    if check_list[sudoku[k+3*i][l+3*j]] == True:
                        result = False
                        break
                    else:
                        check_list[sudoku[k+3*i][l+3*j]] = True

            if result == False:
                break
        if result == False:
                break
    # print("3by3 :", result)
    return result

N = int(input())
results = []
for i in range(1, N+1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    if i != N:
        input()

    result = True if check_row(sudoku) and check_col(sudoku) and check_3by3(sudoku) else False
    results.append(result)

for i in range(1, N+1):
    result = results[i-1]
    if result == True:
        print(f"CASE {i}: CORRECT")
    else:
        print(f"CASE {i}: INCORRECT")
# 1
# 3 5 7 9 6 4 2 8 1
# 4 6 8 1 2 3 5 7 9
# 9 1 2 5 8 7 4 6 3
# 6 3 1 7 9 5 8 4 2
# 7 2 4 3 1 8 6 9 5
# 8 9 5 2 4 6 1 3 7
# 1 7 6 4 5 9 3 2 8
# 5 8 3 6 7 2 9 1 4
# 2 4 9 8 3 1 7 5 6
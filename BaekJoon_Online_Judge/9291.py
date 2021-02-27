import sys

def input_sudoku_map():
    sudoku_map = []
    for _ in range(9):
        sudoku_line = list(map(int, sys.stdin.readline().split()))
        sudoku_map.append(sudoku_line)

    try:
        input()
    except Exception:
        pass

    return sudoku_map

def check_rows(sudoku_map):
    for sudoku_line in sudoku_map:
        counts = [0] * 10
        for num in sudoku_line:
            counts[num - 1] += 1

        if max(counts) != 1:
            return False

    return True


def check_columns(sudoku_map):
    for sudoku_row in range(9):
        counts = [0] * 10
        for sudoku_column in range(9):
            counts[sudoku_map[sudoku_column][sudoku_row]] += 1

        if max(counts) != 1:
            return False

    return True

def check_3x3_squares(sudoku_map):
    for sudoku_row in range(0, 9, 3):
        for sudoku_column in range(0, 9, 3):
            counts = [0] * 10

            for i in range(3):
                for j in range(3):
                    counts[sudoku_map[sudoku_column + i][sudoku_row + j]] += 1

            if max(counts) != 1:
                return False

    return True



num_of_test_case = int(input())

for i in range(num_of_test_case):
    sudoku_map = input_sudoku_map()

    print(f"Case {i + 1}: ", end="")

    if not check_rows(sudoku_map):
        print("INCORRECT")
        continue

    if not check_columns(sudoku_map):
        print("INCORRECT")
        continue

    if not check_3x3_squares(sudoku_map):
        print("INCORRECT")
        continue

    print("CORRECT")
    
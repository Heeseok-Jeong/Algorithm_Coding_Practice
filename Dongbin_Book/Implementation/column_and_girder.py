class point():
    bo = 0
    gi = 0

def solution(n, build_frame):
    answer = [[]]
    grid = [[point() for _ in range(n)] for _ in range(n)]
    
    for x, y, a, b in build_frame:
        if b == 1:
            if a == 1:
                if possible_bo(grid, x, y): # 해당 위치에 보 설치 가능하면
                    grid[x][y].bo = 1
                    answer.append([x, y, a])
            elif a == 0:
                if possible_gi(grid, x, y): # 해당 위치에 기둥 설치 가능하면
                    grid[x][y].gi = 1
                    answer.append([x, y, a])
        elif b == 0:
            if a == 1: # 보 제거
                grid[x][y].bo = 0
                if 
    
    
    return answer

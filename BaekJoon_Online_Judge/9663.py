def solve(n, depth, result): #칸 수, 현재깊이, 횟수저장
    if depth == n: #깊이가 n과 같아지면 성공적으로 퀸 배치했으므로 +1
        result += 1
        return result
    for i in range(1, n+1):
        if not visited_col[i]: #가로 방문 안한곳 탐색
            if temp: #깊이 탐색이 진행되고 있을 경우
                flag = 0
                for row, col in temp: #이전 좌표들 모두 돌면서 현재 좌표랑 대각인지 확인
                    if abs(depth+1-row)-abs(i-col) == 0: #대각 있으면 플래그 1
                        flag = 1
                if flag == 0: #퀸끼리 가로, 세로, 대각 다 안겹치는 경우 => 탐색 진행
                    visited_col[i] = True
                    temp.append([depth+1, i])
                    result = solve(n, depth+1, result)
                    visited_col[i] = False
                    temp.pop()
            else: #제일 처음 깊이일 때
                visited_col[i] = True
                temp.append([depth+1, i])
                result = solve(n, depth+1, result)
                visited_col[i] = False
                temp.pop()
    return result

#depth+1는 가로, 노드는 세로
n = int(input())
result = 0
depth = 0
visited_col = [False] * (n+1) #가로 탐색용
temp = []
result = solve(n, depth, result)
print(result)

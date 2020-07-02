import sys

def readL(): #출력 함수 세팅
    return sys.stdin.readline()

n, m = map(int, readL().split())
visited = [False]*(n+1) #해당 노드 방문하면 True가 됨
result = [] #결과 저장

def solve(depth, n, m):
    if depth == m: #depth랑 최대 깊이가 같으면 출력함
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if not visited[i]: #방문한 곳은 안들리고 결과에 추가 안함
            visited[i] = True #방문했으므로 트루
            result.append(i) #방문한 값을 결과에 넣음
            solve(depth+1, n, m) #다음깊이로 넘어감
            result.pop() #출력다하고 왓을 경우, 해당 원소 팝
            visited[i] = False #방문 다 했으니까 다시 방문기록 false로 만듦 

solve(0, n, m)

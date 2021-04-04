def rotate_key(key):
    new_key = []
    M = len(key)
    for i in range(M):
        temp = []
        for j in range(M):
            temp.append(key[j][i])
        temp.reverse()
        new_key.append(temp)
    return new_key
    
def check_unlock(key, expanded_lock):
    M, ex_N = len(key), len(expanded_lock)
    N = (ex_N+2)//3
    
    for i in range(2*N-1):
        for j in range(2*N-1):
            for a in range(M):
                for b in range(M):
                    expanded_lock[i+a][j+b] += key[a][b]
            
            count = 0
            for a in range(N-1, 2*N-1):
                for b in range(N-1, 2*N-1):
                    if expanded_lock[a][b] == 1:
                        count += 1
            if count == N**2:
                return True
            
            for a in range(M):
                for b in range(M):
                    expanded_lock[i+a][j+b] -= key[a][b]
    
    return False

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    
    expanded_lock = [[0 for _ in range(N*3 - 2)] for _ in range(N*3 - 2)]
    for i in range(N):
        for j in range(N):
            expanded_lock[N-1 + i][N-1 + j] = lock[i][j]
            
            
    rot = 0
    while not answer and rot < 4:
        answer = check_unlock(key, expanded_lock)
        key = rotate_key(key)
        rot += 1
    
    return answer

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    i = 0
    q = deque([[truck_weights[i], 0]])
    i += 1
    answer += 1
    while q:
        if q[0][1] == bridge_length:
            q.popleft()
            
        for j in range(len(q)):
            q[j][1] += 1
            
        if sum(list(zip(*q))[0]) + truck_weights[i] <= weight and len(q) < bridge_length:
            q.append([truck_weights[i], 0]) #truck, place
            i += 1
        
        answer += 1
    
            
        
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
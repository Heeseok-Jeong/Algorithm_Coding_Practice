import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    
    q = []
    length = len(food_times)
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    
    prev = 0
    total = 0
    
    while total + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        total += (now - prev) * length
        
        length -= 1
        prev = now
        
    q.sort(key = lambda x : x[1])
    answer = q[(k-total)%length][1]    
    
    return answer
    
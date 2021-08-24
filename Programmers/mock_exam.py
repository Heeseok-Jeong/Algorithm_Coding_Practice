def solution(answers):
    n = len(answers)
    way1 = [1,2,3,4,5]
    way2 = [2,1,2,3,2,4,2,5]
    way3 = [3,3,1,1,2,2,4,4,5,5]
    index1 = 0
    index2 = 0
    index3 = 0
    len_way1 = len(way1)
    len_way2 = len(way2)
    len_way3 = len(way3)
    scores = [[1,0],[2,0],[3,0]]

    for i in range(n):
        index1 = i%len_way1
        index2 = i%len_way2
        index3 = i%len_way3
        if way1[index1] == answers[i]:
            scores[0][1] += 1
        if way2[index2] == answers[i]:
            scores[1][1] += 1
        if way3[index3] == answers[i]:
            scores[2][1] += 1

    scores = sorted(scores, key = lambda x:-x[1]) 
    i = 0
    answer = []
    while(i < 3 and scores[i][1] == scores[0][1]):
        answer.append(scores[i][0])
        i += 1

    return answer

answers = list(map(int, input().split(",")))
answer = solution(answers)
for x in answer:
    print(x)

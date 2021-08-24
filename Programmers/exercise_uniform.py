def solution(n, lost, reserve):
    answer = 0
    dupli_list = [x for x in reserve if x in lost]
    print(dupli_list)

    for x in dupli_list:
        lost.remove(x)
        reserve.remove(x)

    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)

    answer = n - len(lost)
    return answer

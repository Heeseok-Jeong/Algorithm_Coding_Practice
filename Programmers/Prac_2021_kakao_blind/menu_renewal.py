from itertools import combinations

def solution(orders, course):
    answer = []
    combi_dict = {}
    for i in course:
        combi_dict[i] = {}
    for order in orders:
        for i in course:
            combis = list(combinations(sorted(order), i))
            for combi in combis:
                combi = ''.join(combi)
                if combi_dict[i].get(combi):
                    combi_dict[i][combi] += 1
                else:
                    combi_dict[i][combi] = 1

    for i in course:
        if not list(combi_dict[i].values()):
            continue
            
        max_v = max(list(combi_dict[i].values()))
        if max_v < 2:
            continue
            
        for k, v in combi_dict[i].items():
            if max_v == v :
                answer.append(k)
    answer.sort()
    return answer
    
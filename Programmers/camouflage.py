def solution(clothes):
    answer = 1
    clothes_dict = {}
    for clothe, category in clothes:
        if clothes_dict.get(category):
            clothes_dict[category] += 1 
        else:
            clothes_dict[category] = 1
    
    for count in clothes_dict.values():
        answer *= count+1
        
    return answer - 1
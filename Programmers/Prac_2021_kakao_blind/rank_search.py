from bisect import bisect_left

def solution(info, query):
    answer = []
    groups_data = {}
    for lang in ["cpp", "java", "python", "-"]:
        for job in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for soul_food in ["chicken", "pizza", "-"]:
                    groups_data[" ".join([lang, job, career, soul_food])] = []
    
    for line in info:
        lang, job, career, soul_food, score = line.split()
        lang_arr = ['-', lang] if lang != '-' else ['-']
        job_arr = ['-', job] if job != '-' else ['-']
        career_arr = ['-', career] if career != '-' else ['-']
        soul_food_arr = ['-', soul_food] if soul_food != '-' else ['-']
        
        for lang in lang_arr:
            for job in job_arr:
                for career in career_arr:
                    for soul_food in soul_food_arr:
                        groups_data[" ".join([lang, job, career, soul_food])].append(int(score))
    
    for k, v in groups_data.items():
        groups_data[k] = sorted(v)
    
    for line in query:
        lang, job, career, soul_food_score = line.split(' and ')
        soul_food, score = soul_food_score.split()
        lower_index = bisect_left(groups_data[" ".join([lang, job, career, soul_food])], int(score))
        answer.append(len(groups_data[" ".join([lang, job, career, soul_food])]) - lower_index)
    return answer
    
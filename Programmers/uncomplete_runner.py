from collections import Counter

def solution(participant, completion):
#     answer = ''
#     vocab = {}
#     for name in participant:
#         if vocab.get(name):
#             vocab[name] += 1
#         else:
#             vocab[name] = 1
    
#     for name in completion:
#         vocab[name] -= 1
        
#     for name, count in vocab.items():
#         if count == 1:
#             answer = name
#     return answer
    
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

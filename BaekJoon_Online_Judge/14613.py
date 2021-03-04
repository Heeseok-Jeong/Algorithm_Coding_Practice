# W, L, D = map(float, input().split())

# probs = [0] * 5

# def fac(x):
#     if x <= 1:
#         return 1

#     return x * fac(x-1)

# for num_w in range(21):
#     for num_l in range(21-num_w):
#         num_d = 20 - num_w - num_l 
#         score = 2000 + num_w*50 - num_l*50
#         rank = score // 500 - 2
#         cases = fac(20) // fac(num_w) // fac(num_l) // fac(num_d)
#         probs[rank] += (W**num_w) * (L**num_l) * (D**num_d) * cases

# for prob in probs:
#     print("%.8f" % prob)

from itertools import combinations
W, L, D = map(float, input().split())

probs = [0] * 5

def fac(x):
    if x <= 1:
        return 1

    return x * fac(x-1)

for num_w in range(21):
    for num_l in range(21-num_w):
        num_d = 20 - num_w - num_l 
        score = 2000 + num_w*50 - num_l*50
        rank = score // 500 - 2
        cases = fac(20) // fac(num_w) // fac(num_l) // fac(num_d)
        probs[rank] += (W**num_w) * (L**num_l) * (D**num_d) * len(tuple(combinations([i for i in range(20)], num_w))) * len(tuple(combinations([i for i in range(20-num_w)], num_l)))

for prob in probs:
    print("%.8f" % prob)



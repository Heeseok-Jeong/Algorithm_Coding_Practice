from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())

VOWELS = ['a', 'e', 'i', 'o', 'u']
v_arr = []
c_arr = []

for a in arr:
    if a in VOWELS:
        v_arr.append(a)
    else:
        c_arr.append(a)

passwords = []
for v_num in range(1, L-2 + 1):
    if v_num > len(v_arr):
        continue

    c_num = L - v_num
    alphas = []
    v_combis = list(combinations(v_arr, v_num))
    c_combis = list(combinations(c_arr, c_num))
    for v_c in v_combis:
        for c_c in c_combis:
            alphas = sorted(list(v_c + c_c))
            password = ''.join(alphas)
            passwords.append(password)

for password in sorted(passwords):
    print(password)
    
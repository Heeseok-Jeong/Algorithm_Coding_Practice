N = input()
N_len = len(N)
result = ["LUCKY", "READY"]
front = sum(list(map(int, N[:N_len//2])))
back = sum(list(map(int, N[N_len//2:])))
if front == back:
    print(result[0])
else:
    print(result[1])

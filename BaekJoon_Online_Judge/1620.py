import sys

input = sys.stdin.readline

N, M = map(int, input().split())

name_vocab = {}
num_vocab = {}
for i in range(1, N+1):
    name = input().rstrip()
    name_vocab[name] = i
    num_vocab[i] = name

for _ in range(M):
    is_name = True
    user_input = input().rstrip()
    try:
        user_input = int(user_input)
        is_name = False
    except ValueError:
        pass

    result = name_vocab[user_input] if is_name else num_vocab[user_input]
    
    print(result)
    
from math import log2

def shuffle(cards, e):
    left, right = cards[:-2**e], cards[len(cards)-2**e:]
    
    if e == 0:
        return right + left
    
    return shuffle(right, e-1) + left

N = int(input())
answer_cards = input().split()
max_K = int(log2(N))
if 2**max_K == N:
    max_K -= 1
cards = [str(n+1) for n in range(N)]
answer_found = False

for first_K in range(max_K, 0, -1):
    first_shuffled_cards = shuffle(cards, first_K)
    for second_K in range(max_K, 0, -1):
        second_shuffled_cards = shuffle(first_shuffled_cards, second_K)
        if answer_cards == second_shuffled_cards:
            answer_found = True
            break
    if answer_found:
        break

print(first_K, second_K)

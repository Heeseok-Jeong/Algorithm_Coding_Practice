N = int(input())
N -= 1

words = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu',
        'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']

tururu = [2, 6, 10]
turu = [3, 7, 11]

a = N//14
r = N%14

answer = ""
if r in tururu+turu:
    k = 2 + a if r in tururu else 1 + a
    answer = "tu" + "ru"*k if k < 5 else f"tu+ru*{k}"
else:
    answer = words[r]

print(answer)

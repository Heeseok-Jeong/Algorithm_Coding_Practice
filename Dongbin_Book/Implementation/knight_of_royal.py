starting = input()
x = int(starting[1])
y = ord(starting[0])-96
point = [x, y]
answer = 0

double = [2, -2]
one = [1, -1]

for i in range(2):
    for j in range(2):
        x, y = point
        x += double[i]
        y += one[j]
        if not (x < 1 or y < 1 or x > 8 or y > 8):
            answer += 1
for i in range(2):
    for j in range(2):
        x, y = point
        y += double[i]
        x += one[j]
        if not (x < 1 or y < 1 or x > 8 or y > 8):
            answer += 1
print(answer)

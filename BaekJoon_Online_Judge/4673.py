def d(n): #932, 12, 5
    sum = n
    temp = n
    while temp//10 != 0:
        sum += temp%10
        temp //= 10
    sum += temp
    return sum

b_list = []

for i in range(1, 10001):
    b_list.append(i)

for i in range(1, 10001):
    for j in b_list:
        if d(i)==j:
            b_list.remove(d(i))
            break


for i in b_list:
    print(i)

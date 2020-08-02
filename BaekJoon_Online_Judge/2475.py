n_list = map(int, input().split())
result = 0
for n in n_list:
    temp = n**2
    result += temp
result %= 10
print(result)

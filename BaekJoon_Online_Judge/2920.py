n_list = list(map(int, input().split()))
flag = 0
length = len(n_list)
for i in range(length-1):
    if n_list[0] == 1:
        if n_list[i] == n_list[i+1]-1:
            flag = 0
            continue
        else:
            flag = 2
            break
    else:
        if n_list[i] == n_list[i+1]+1:
            flag = 1
            continue
        else:
            flag = 2
            break

if flag == 0:
    print("ascending")
elif flag == 1:
    print("descending")
else:
    print("mixed")

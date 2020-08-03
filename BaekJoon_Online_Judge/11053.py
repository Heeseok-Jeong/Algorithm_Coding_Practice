def solve(memo, index):
    print("index :", index)
    count = len(memo)
    count_2 = 0
    last = memo[-1]
    for i in range(index, len(n_list)):
        n = n_list[i]
        print("last :", last, ", n :", n)
        if last > n:
            for j in range(len(memo)):
                n_2 = memo[j]
                if n_2 == n:
                    break
                if n_2 > n:
                    temp = memo[:j]
                    temp.append(n)
                    print(temp)
                    count_2 = solve(temp, i+1)
                    print("count :", count, ", count2 :", count_2)
                    if count < count_2:
                        count = count_2
                        print("new_count :", count)
                    #     return count
                    break

        elif last < n:
            last = n
            memo.append(n)
            count += 1
            print("add :", memo)

    if count < count_2:
        count = count_2
        print("new_count :", count)
    return count

n = int(input())
n_list = list(map(int, input().split()))
memo = []
memo.append(n_list[0])
index = 1
result = solve(memo, index)
print(result)

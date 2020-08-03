def solve(memo):
    count = 0
    last = n_list[-1]
    for n in n_list:
        if last > n:
            for i in range(len(memo)):
                n_2 = memo[i]
                if n_2 == n:
                    break
                if n_2 < n:
                    temp = memo[:i]
                    temp.append(n_2)
                    count_2 = solve(temp)
                    if count < count_2:
                        count = count_2
                        return count
                    break

        elif last < n:
            last = n
            memo.append(n)
            count += 1
        print(memo)

    return count

n = int(input())
n_list = list(map(int, input().split()))
memo = []
memo.append(n_list[0])
result = solve(memo)
print(result)

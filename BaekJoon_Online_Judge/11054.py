def count_first(k, seq, memo):
    length = len(seq)
    for i in range(length):
        n = seq[i]
        if n <= k:
            continue
        elif i == 0:
            memo[i] = 1
        else:
            temp = 1
            for j in range(i):
                m = seq[j]
                if m <= k:
                    continue
                if m < n and temp <= memo[j]:
                    temp = memo[j]+1
            memo[i] = temp

def count_last(k, seq, memo):
    length = len(seq)
    for i in range(length):
        n = seq[i]
        if n <= k:
            continue
        elif i == 0:
            memo[i] = 1
        else:
            temp = 1
            for j in range(i):
                m = seq[j]
                if m <= k:
                    continue
                if m > n and temp <= memo[j]:
                    temp = memo[j]+1
            memo[i] = temp


def count_left(k, seq, memo):
    length = len(seq)
    for i in range(length):
        n = seq[i]
        if n >= k:
            continue
        elif i == 0:
            memo[i] = 1
        else:
            temp = 1
            for j in range(i):
                m = seq[j]
                if m >= k:
                    continue
                if m < n and temp <= memo[j]:
                    temp = memo[j]+1
            memo[i] = temp

def count_right(k, seq, memo):
    length = len(seq)
    for i in range(length):
        n = seq[i]
        if n >= k:
            continue
        elif i == 0:
            memo[i] = 1
        else:
            temp = 1
            for j in range(i):
                m = seq[j]
                if m >= k:
                    continue
                if m > n and temp <= memo[j]:
                    temp = memo[j]+1
            memo[i] = temp

def solve():
    for i in range(length):
        k = seq[i]
        temp = 1
        l_seq = seq[:i]
        l_memo = [0 for _ in range(i)]
        r_seq = seq[i+1:length+1]
        r_memo = [0 for _ in range(length-i-1)]
        if i == 0:
            count_first(k, r_seq, r_memo)
            temp += max(r_memo)
        elif i == length-1:
            count_last(k, l_seq, l_memo)
            temp += max(l_memo)
        else:
            count_left(k, l_seq, l_memo)
            temp += max(l_memo)
            count_right(k, r_seq, r_memo)
            temp += max(r_memo)
        memo[i] = temp

length = int(input())
seq = list(map(int, input().split()))
if length == 1:
    print(1)
else:
    memo = [0 for _ in range(length)]
    solve()
    result = max(memo)
    print(result)

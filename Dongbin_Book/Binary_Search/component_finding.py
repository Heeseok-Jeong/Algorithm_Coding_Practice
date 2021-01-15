import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()
m = int(input())
m_arr = list(map(int, input().split()))

for item in m_arr:
    s, e = 0, n-1
    finded = False
    while s <= e:
        mid = (s+e) // 2
        if n_arr[mid] == item:
            finded = True
            break
        elif n_arr[mid] > item:
            e = mid - 1
        else:
            s = mid + 1
    if finded:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')

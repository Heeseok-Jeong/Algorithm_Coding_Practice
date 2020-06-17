import sys

def hanoi(n, f, t, o):
    if(n==0):
        return
    else:
        hanoi(n-1, f, o, t)
        temp = str(f) + " " + str(t)
        a.append(temp)
        hanoi(n-1, o, t, f)

a = []
n = int(sys.stdin.readline())
hanoi(n, 1, 3, 2)
print(len(a))
for i in a:
    print(i)

import sys

def hs(x):
    if x < 100:
        return True
    elif x == 1000:
        return False
    else:
        a = x//100
        temp = x%100
        b = temp//10
        c = temp%10
        dif1 = a - b
        dif2 = b - c
        if dif1 == dif2:
            return True
        else:
            return False

x = int(sys.stdin.readline())
count = 0

for i in range(1, x+1):
    count += hs(i)
print(count)

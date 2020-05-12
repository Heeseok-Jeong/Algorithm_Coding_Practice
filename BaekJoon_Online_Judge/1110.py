import sys

x = int(sys.stdin.readline())
new = x
a = 0
y = 0
count = 0

while x!=y:
    a = new//10 + new%10
    # print(a)
    new = (new%10)*10 + a%10
    # print(new)
    y = new
    count += 1
    # print(y)
if x == 0:
    count = 1
print(count)

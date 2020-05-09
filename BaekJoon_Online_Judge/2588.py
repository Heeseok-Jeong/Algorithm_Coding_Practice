a = int(input())
b = int(input())

b_000 = b//100
t2 = b%100
b_00 = t2//10
t2 = b%10
b_0 = t2

print(a*b_0)
print(a*b_00)
print(a*b_000)
print(a*b)

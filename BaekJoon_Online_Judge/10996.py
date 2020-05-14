import sys

n = int(sys.stdin.readline())

if n == 1:
    print("*")
else:
    for i in range(1, n+1):
        str1 = ""
        str2 = ""

        for j in range(1, n+1):
            if j%2 == 1:
                str1 += "* "
            else:
                str2 += " *"
        print(str1)
        print(str2)

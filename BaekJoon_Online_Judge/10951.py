import sys

while True:
    try:
        str = sys.stdin.readline()
        a, b = map(int, str.split())
        print(a+b)
    except:
        exit()

import sys

input  = sys.stdin.readline

M = int(input())

m_set = set()
for _ in range(M):
    op, num = 0, 0
    user_input = input().rstrip()
    if user_input not in  ["all", "empty"]:
        op, num = user_input.split()
    else:
        op = user_input
    num = int(num)

    if op == "add":
        m_set.add(num)
    elif op == "remove":
        if num in m_set:
            m_set.remove(num)
    elif op == "check":
        if num in m_set:
            print(1)
        else:
            print(0)
    elif op == "toggle":
        if num in m_set:
            m_set.remove(num)
        else:
            m_set.add(num)
    elif op == "all":
        m_set = set([i for i in range(1, 21)])
    elif op == "empty":
        m_set.clear()

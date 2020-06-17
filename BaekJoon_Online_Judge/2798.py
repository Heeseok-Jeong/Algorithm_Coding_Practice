import sys
from itertools import combinations as combi

def readL():
    return sys.stdin.readline()

#1. nC3으로 조합 다 구함 (가능하면 2개 조합해서 넘으면 컷)
#2. 조합 중 m 넘는거 삭제
#3. 남은거 중에서 맥스함수 리턴
def BlackJack(m, a):
    temp = combi(a, 3)
    for i in temp:
        sum_i = sum(i)
        if sum_i <= m:
            b.append(sum(i))
    return max(b)

n, m = map(int, readL().split())
a = list(map(int, readL().split()))
b = []
print(BlackJack(m, a))

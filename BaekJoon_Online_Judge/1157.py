import sys

x = sys.stdin.readline()
a_list = [0] * 26
index = 0

for i in x:
    for j in range(0, 26):
        if i == chr(j+65) or i == chr(j+97):
            a_list[j] += 1

a_max = max(a_list)
count = 0
for i in range(0, len(a_list)):
    if a_max == a_list[i]:
        count += 1
        index = i

if count != 1:
    print("?")
else:
    print(chr(index+65))

from collections import Counter

word = input().upper()
# print(word)
most_list = Counter(list(word)).most_common()
most_alpha = most_list[0][0]

for i in range(1, len(most_list)):
    if most_list[0][1] == most_list[i][1]:
        # print("aa")
        most_alpha = '?'
        break
# print(most_list)
print(most_alpha)

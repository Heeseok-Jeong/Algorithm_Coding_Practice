# def solution(brown, yellow):
#     answer = []
#     yellow_form = []
#     for row in range(1, yellow+1):
#         if(yellow % row == 0):
#             col = yellow//row
#             if row < col:
#                 continue
#             yellow_form.append([row, col])

#     for row, col in yellow_form:
#         if brown == (row+2)*(col+2)-row*col:
#             answer.append(row+2)
#             answer.append(col+2)
#             break
#     return answer

# brown, yellow = map(int, input().split())
# answer = solution(brown, yellow)
# print(answer)

def solution(brown, yellow):
    answer = 0
    for y in range(1, int(yellow**0.5) + 1):
        if yellow % y == 0:
            if 2*(yellow//y + y) + 4 == brown:
                answer = [yellow//y + 2, y + 2]
                break
    return answer
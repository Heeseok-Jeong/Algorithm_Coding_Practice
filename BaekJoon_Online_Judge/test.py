# def solution(n, m, dusts, walls, winds):
#     answer = 0
#     mat = [[0 for col in range(m)] for row in range(n)]
#     # set walls
#     mat = setWalls(mat, walls)
#     # set dusts
#     mat = setDusts(mat, dusts)
#     # print("Before :", str(mat))
#     # extend dusts
#     ext(mat, winds, n, m)
#     # check num
#     answer = checkNum(mat)
#
#     # print("After  :", str(mat))
#     return answer
#
# def setWalls(mat, walls):
#     for i in walls:
#         mat[i[0]-1][i[1]-1] = 2
#     return mat
#
# def setDusts(mat, dusts):
#     for i in dusts:
#         mat[i[0]-1][i[1]-1] = 1
#     return mat
#
# def ext(mat, winds, n, m):
#     for a in winds:
#         temp = []
#         if a == 'E':
#             for i in range(0, n):
#                 for j in range(0, m):
#                     if j>0:
#                         if mat[i][j] == 1 and mat[i][j-1] != 2:
#                             temp.append((i, j-1))
#         elif a == 'W':
#             for i in range(0, n):
#                 for j in range(0, m):
#                     if j<m-1:
#                         if mat[i][j] == 1 and mat[i][j+1] != 2:
#                             temp.append((i, j+1))
#         elif a == 'S':
#             for i in range(0, n):
#                 if i>0:
#                     for j in range(0, m):
#                         if mat[i][j] == 1 and mat[i-1][j] != 2:
#                                 # print(i , j)
#                                 temp.append((i-1, j))
#         else:
#             for i in range(0, n):
#                 if i<n-1:
#                     for j in range(0, m):
#                         if mat[i][j] == 1 and mat[i+1][j] != 2:
#                             temp.append((i+1, j))
#         # print(temp)
#         for b in temp:
#             mat[b[0]][b[1]] = 1
#         # print(a, str(mat))
#         # print()
#     return mat
#
# def checkNum(mat):
#     count = 0
#     for i in mat:
#         for j in i:
#             if j == 1:
#                 count += 1
#     return count
#
#
# n = 3
# m =  3
# dusts =  [[1,3],[3,1]]
# walls =  [[2,2]]
# winds =  ["W", "S", "S", "E", "N"]
# print(solution(n, m, dusts, walls, winds))


def solution(ages, wires):
    temp = ages
    m = max(ages)
    answer = []
    state = [1] * len(ages)


    for i in range(1, m+1):
        for j in range(0, len(ages)):
            temp[j] -= 1
            if temp[j] <= 0 and state[j] == 1:
                for x in wires:
                    if x[1] == j:
                        if temp[x[0]]+x[2] > 0:
                            state[j] = 1
                        else:
                            state[j] = 0
                            answer.append(j+1)


    return answer

ages = [35,25,3,8,7]
wires = [[1,2,5],[2,1,5],[1,3,2],[3,4,2],[3,5,20],[4,5,1]]
print(solution(ages, wires))

import heapq

a = []
heapq.heappush(a, (5,1))
heapq.heappush(a, (2,4))
heapq.heappush(a, (5,3))
heapq.heappush(a, (1,2))
heapq.heappush(a, (2,3))
heapq.heappush(a, (8,1))
print(a)
for _ in range(len(a)):
    print(heapq.heappop(a))
# def browse(count, ap_index):
#     global route_index
#     global info
#     global ticket_size
#     global ap_size
#     print("count :", count, ", ap_index :", ap_index)
#     route_index.append(ap_index)
#
#     is_all_zero = True
#     for x in info[ap_index]:
#         if x > 0:
#             is_all_zero = False
#
#     if is_all_zero:
#         if count == ticket_size:
#             return True
#         else:
#             route_index.pop()
#             return False
#
#     for i in range(ap_size):
#         if info[ap_index][i] > 0:
#             info[ap_index][i] -= 1
#             result = browse(count+1, i)
#             print(result)
#             if not result:
#                 info[ap_index][i] += 1
#             else:
#                 return True
#
#
# route_index = []
# info = []
# ticket_size = 0
# ap_size = 0
#
# def solution(tickets):
#     global route_index
#     global info
#     global ticket_size
#     global ap_size
#     answer = []
#     ticket_size = len(tickets)
#     ap_names = set()
#     for start, to in tickets:
#         ap_names.add(start)
#         ap_names.add(to)
#     ap_names = sorted(list(ap_names))
#     print("ap_names :", ap_names)
#     ap_size = len(ap_names)
#     info = [[0 for _ in range(ap_size)] for _ in range(ap_size)]
#
#     for start, to in tickets:
#         start_index = ap_names.index(start)
#         to_index = ap_names.index(to)
#         info[start_index][to_index] += 1
#     print("info :", info)
#     print("ticket_size :", ticket_size)
#
#     ap_index = ap_names.index("ICN")
#     count = 0
#     browse(count, ap_index)
#
#     for i in route_index:
#         answer.append(ap_names[i])
#
#     return answer
#
# # def browse(d, ticket_size, answer, info, stack, ap_names):
# #     if d == ticket_size:
# #         is_completed = True
# #         return answer
# #
# #     while stack:
# #         start_index = stack.pop()
# #         if sum(info[start_index]) == 0:
# #             info[start_index]
# #         answer.append(ap_names[start_index])
# #         for i in range(len(info)):
# #             if info[start_index][i] == 1:
# #                 stack.append(i)
# #
# #
# #
# #
# #
# # is_completed = False
# #
# # def solution(tickets):
# #     answer = []
# #     ap_names = set()
# #     for start, to in tickets:
# #         ap_names.add(start)
# #         ap_names.add(to)
# #     ap_names = sorted(list(ap_names))
# #     print("ap_names :", ap_names)
# #     ap_size = len(ap_names)
# #     info = [[0 for _ in range(ap_size)] for _ in range(ap_size)]
# #
# #     for start, to in tickets:
# #         start_index = ap_names.index(start)
# #         to_index = ap_names.index(to)
# #         info[start_index][to_index] = 1
# #     print("info :", info)
# #
# #     stack = []
# #     start_index = ap_names.index("ICN")
# #     stack.append(start_index)
# #     ticket_size = len(tickets)
# #     d = 0
# #     answer = browse(d, ticket_size, answer, info, stack, ap_names)
# #
# #     return answer

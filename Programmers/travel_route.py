def solution(tickets):
    answer = []
    routes = {}
    for start, to in tickets:
        routes[start] = routes.get(start, []) + [to]

    print("routes :", routes)
    for key in routes.keys():
        print("key :", key)
        # routes[key].sort(reverse = True)
        routes[key] = sorted(routes[key], reverse = True)
    print("routes :", routes)

    stack = ["ICN"]
    while stack:
        top = stack[-1]

        if top not in routes or not routes[top]:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top].pop()

    answer.reverse()

    return answer

while True:
    a = input()

    if a == "0":
        break

    len_a = len(a)
    
    n = len_a // 2
    result = "yes"
    for i in range(n):
        if a[i] != a[len_a-1-i]:
            result = "no"

    print(result)

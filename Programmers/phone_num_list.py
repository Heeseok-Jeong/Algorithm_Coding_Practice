def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        pivot = phone_book[i]
        next = phone_book[i+1]
        pivot_len = len(pivot)
        next_len = len(next)
        if  pivot_len <= next_len:
            if pivot == next[:pivot_len]:
                answer = False
                break
            
    return answer
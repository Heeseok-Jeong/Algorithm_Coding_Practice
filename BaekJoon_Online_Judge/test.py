for i in range(1, 10):
    if 2<i<4:
        print(i)
        break
    else:
        print("a")
else:
    print("end of loop. not found")

for i in range(1, 10):
    if 2<i<3:
        print(i)
        break
    else:
        print("b")
else:
    print("end of loop. not found")

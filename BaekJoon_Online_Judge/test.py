import dis
print(4 != 0 not in [1, 2, 3])
dis.dis('print(4 != 0 not in [1, 2, 3])')
print((4 != 0) not in [1, 2, 3])
dis.dis('print((4 != 0) not in [1, 2, 3])')
print(4 != 0 not in [0, 1, 2, 3])
dis.dis('print(4 != 0 not in [0, 1, 2, 3])')
print((4 != 0) not in [0, 1, 2, 3])
dis.dis('print((4 != 0) not in [0, 1, 2, 3])')
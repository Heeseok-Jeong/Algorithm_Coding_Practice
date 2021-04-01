S = input()
character = []
num = 0
for c in S:
    try:
        num += int(c)
    except:
        character.append(c)
character.sort()
character += str(num)

print("".join(character))

f = open('2022/day6input.txt', 'r').readlines()
stream = f[0]
# switch out 14 for x length of messages
for x in range(len(stream)):
    unique = []
    if x + 14 <= len(stream):
        temp = stream[x: x+14]
    else:
        break
    for c in temp:
        if c not in unique:
            unique.append(c)
        else:
            break
    if len(unique) == 14:
        print(temp, x+14)
        break
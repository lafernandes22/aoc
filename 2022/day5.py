f = open('2022/day5input.txt', 'r').readlines()
lines = []

for line in f:
    line = line.replace('\n', '')
    lines.append(line)

stacks = {}
stacks[0] = ['W', 'M', 'L', 'F']
stacks[1] = ['B', 'Z', 'V', 'M', 'F']
stacks[2] = ['H', 'V', 'R', 'S', 'L', 'Q']
stacks[3] = ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J']
stacks[4] = ['L', 'S', 'W']
stacks[5] = ['F', 'V', 'P', 'M', 'R', 'J', 'W']
stacks[6] = ['J', 'Q', 'C', 'P', 'N', 'R', 'F']
stacks[7] = ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B']
stacks[8] = ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']


for line in lines:
    line = line.split(' ')
    if len(line) > 0 and line[0] == 'move':
        num = int(line[1])
        s = int(line[3])
        e = int(line[5])
        sStack = stacks[s-1]
        temp = sStack[len(sStack)-num:]
        # temp.reverse() pt1
        eStack = stacks[e-1]
        print('before', stacks[s-1], stacks[e-1])
        for i in temp:
            sStack.pop()
            eStack.append(i)
        stacks[s-1] = sStack
        stacks[e-1] = eStack
        print('after', stacks[s-1], stacks[e-1])

print(stacks)
res = ""
for s in stacks:
    res += stacks[s][len(stacks[s])-1]

print(res)
f = open('2022/day10test.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    lines.append(line)

val = 1
queue = []
length = 0
for line in lines:
    line = line.split(' ')
    match(line[0]):
        case 'addx':
            length += 2
        case 'noop':
            length += 1
for counter in range(length):
    if counter < len(lines):
        line = lines[counter].split(' ')
        match(line[0]):
            case 'addx':
                curr_item = (counter + 2, int(line[1]))
                queue.append(curr_item)
    else:
        break
for counter in range(length):
    if queue:
        if queue[0][0] == counter:
            val += queue[0][1]
            queue.pop(0)
    test = [19, 59, 99, 139, 179, 219]
    if counter in range(0,20):
        print(counter+1, val)


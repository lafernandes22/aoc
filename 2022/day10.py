f = open('2022/day10input.txt', 'r').readlines()
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
counter = 0
count = 0
sum = 0
while counter != length:
    if count < len(lines):
        line = lines[count].split(' ')
        match(line[0]):
            case 'addx':
                curr_item = (counter + 2, int(line[1]))
                queue.append(curr_item)
                counter += 2
            case 'noop':
                counter += 1
        count += 1
    else:
        break
for counter in range(length):
    if queue:
        if queue[0][0] == counter:
            val += queue[0][1]
            queue.pop(0)
    test = [19, 59, 99, 139, 179, 219]
    if counter in test:
        print(counter+1, val)
        sum += val * (counter + 1)
print(sum)


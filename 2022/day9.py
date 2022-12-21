f = open('2022/day9test.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    line = line.split(' ')
    lines.append(line)

length, width = 100, 100
start_pos = [length/2, width/2]
head_pos = start_pos
tail_pos = start_pos

for line in lines:
    match(line[0]): # Setting Head pos
        case 'R':
            head_pos = (head_pos[0], head_pos[1] + line[1])
        case 'L':
            head_pos = (head_pos[0], head_pos[1] - line[1])
        case 'U':
            head_pos = (head_pos[0] + line[1], head_pos[1])
        case 'D':
            head_pos = (head_pos[0] - line[1], head_pos[1])
    # TODO calculate shortest omni path from Tail to Head
    # A Star scoring movement options
    



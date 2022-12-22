f = open('2022/day9input.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    line = line.split(' ')
    lines.append(line)

length, width = 5, 6
# start_pos = (length//2, width//2)
start_pos = (0,0)
head_pos = start_pos
tail_pos = start_pos
visited = [tail_pos]

def check_distance(head, tail):
    if not -1 <= head[0] - tail[0] <= 1 or not -1 <= head[1] - tail[1] <= 1:
        return False
    else:
        return True
def check_ordinal(head, tail):
    if head[0] - tail[0] != 0 and head[1] - tail[1] != 0:
        return False
    else:
        return True

def print_board():
    for x in range(length-1, -1, -1):
        line = ''
        line_pos = ''
        for y in range(width):
            if (x,y) in visited:
                line += '#'
                if (x,y) == tail_pos:
                    line_pos += 'T'
                else:
                    line_pos += '.'
            elif (x,y) == head_pos:
                 line_pos += 'H'
                 line += '.'
            else:
                line += '.'
                line_pos += '.'
        # print(line, line_pos)

for line in lines:
    # TODO loop each motion and every step move tail as needed, track seen positions at each step
    print('  == '+''.join(line)+' ==')
    # TODO ordinal check to move tail diagonally to reset to ordinal movement
    match(line[0]): 
        case 'R':
            for x in range(int(line[1])):
                head_pos = (head_pos[0], head_pos[1] + 1)
                if not check_distance(head_pos, tail_pos):
                    tail_pos = (tail_pos[0], tail_pos[1] + 1)
                    if not check_ordinal(head_pos, tail_pos):
                        tail_pos = (head_pos[0], tail_pos[1])
                    if tail_pos not in visited:
                        visited.append(tail_pos)
                        print_board()
        case 'L':
           for x in range(int(line[1])):
                head_pos = (head_pos[0], head_pos[1] - 1)
                if not check_distance(head_pos, tail_pos):
                    tail_pos = (tail_pos[0], tail_pos[1] - 1)
                    if not check_ordinal(head_pos, tail_pos):
                        tail_pos = (head_pos[0], tail_pos[1])
                    if tail_pos not in visited:
                        visited.append(tail_pos)
                        print_board()
        case 'U':
            for x in range(int(line[1])):
                head_pos = (head_pos[0] + 1, head_pos[1])
                if not check_distance(head_pos, tail_pos):
                    tail_pos = (tail_pos[0] + 1, tail_pos[1])
                    if not check_ordinal(head_pos, tail_pos):
                        tail_pos = (tail_pos[0], head_pos[1])
                    if tail_pos not in visited:
                        visited.append(tail_pos)
                        print_board()
        case 'D':
            for x in range(int(line[1])):
                head_pos = (head_pos[0] - 1, head_pos[1])
                if not check_distance(head_pos, tail_pos):
                    tail_pos = (tail_pos[0] - 1, tail_pos[1])
                    if not check_ordinal(head_pos, tail_pos):
                        tail_pos = (tail_pos[0], head_pos[1])
                    if tail_pos not in visited:
                        visited.append(tail_pos)
                        print_board()
print_board()
print(len(visited))  




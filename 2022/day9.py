f = open('2022/day9test.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    line = line.split(' ')
    lines.append(line)

length, width = 100, 100
start_pos = (length//2, width//2)
head_pos = start_pos
tail_pos = start_pos
visited = []

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
        print(line, line_pos)

def pt1():
    visited.append(tail_pos)
    for line in lines:
        print('  == '+''.join(line)+' ==')
        match(line[0]): 
            case 'R':
                for _ in range(int(line[1])):
                    head_pos = (head_pos[0], head_pos[1] + 1)
                    if not check_distance(head_pos, tail_pos):
                        tail_pos = (tail_pos[0], tail_pos[1] + 1)
                        if not check_ordinal(head_pos, tail_pos):
                            tail_pos = (head_pos[0], tail_pos[1])
                        if tail_pos not in visited:
                            visited.append(tail_pos)
                            print_board()
            case 'L':
                for _ in range(int(line[1])):
                        head_pos = (head_pos[0], head_pos[1] - 1)
                        if not check_distance(head_pos, tail_pos):
                            tail_pos = (tail_pos[0], tail_pos[1] - 1)
                            if not check_ordinal(head_pos, tail_pos):
                                tail_pos = (head_pos[0], tail_pos[1])
                            if tail_pos not in visited:
                                visited.append(tail_pos)
                                print_board()
            case 'U':
                for _ in range(int(line[1])):
                    head_pos = (head_pos[0] + 1, head_pos[1])
                    if not check_distance(head_pos, tail_pos):
                        tail_pos = (tail_pos[0] + 1, tail_pos[1])
                        if not check_ordinal(head_pos, tail_pos):
                            tail_pos = (tail_pos[0], head_pos[1])
                        if tail_pos not in visited:
                            visited.append(tail_pos)
                            print_board()
            case 'D':
                for _ in range(int(line[1])):
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

rope = {}
for x in range(1, 10):
    rope[x] = head_pos


def move (head, tail, dir): # checking if tail needs to move relative to head
    print(head, tail)
    match(dir):
        case 'R':
            if not check_distance(head, tail):
                tail = (tail[0], tail[1] + 1)
                if not check_ordinal(head, tail):
                    tail = (head[0], tail[1])
                return True
        case 'L':
            if not check_distance(head, tail):
                tail = (tail[0], tail[1] - 1)
                if not check_ordinal(head, tail):
                    tail = (head[0], tail[1])
                return True
        case 'U':
            if not check_distance(head, tail):
                tail = (tail[0] + 1, tail[1])
                if not check_ordinal(head, tail):
                    tail = (tail[0], head[1])
                return True
        case 'D':
            if not check_distance(head, tail):
                tail = (tail[0] - 1, tail[1])
                if not check_ordinal(head, tail):
                    tail = (tail[0], head[1])
                return True
    return False

def print_board_pt2():
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
        print(line, line_pos)

for line in lines:
    print('  == '+''.join(line)+' ==')
    dir = line[0]
    tail_key = 1
    visited.append(rope[9])
    match(dir):
        case 'R':
            for _ in range(int(line[1])):
                head_pos = (head_pos[0], head_pos[1] + 1)
                curr_tail = rope[tail_key]
                print(tail_key)
                while move(head_pos, curr_tail, dir): # TODO: return new tail pos if true to modify
                    if tail_key == 9 and curr_tail not in visited:
                        visited.append(tail_key)
                    tail_key += 1
                    if tail_key == 10:
                        break
                    else:
                        curr_tail = rope[tail_key]
                tail_key += 1
                print(tail_key)
    break



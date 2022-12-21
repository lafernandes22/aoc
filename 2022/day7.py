from collections import Counter

f = open('2022/day7input.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    lines.append(line)

dirs = {}
current_route = []
for line in lines:
    line = line.split(' ')
    match(line[0]):
        case '$':
            match(line[1]):
                case 'cd':
                    match(line[2]):
                        case '..':
                            current_route.pop()
                        case default:
                            current_route.append(line[2] if line[2] == '/' else line[2] + '/') 
                            current_route_str = ''.join(current_route)
                            if current_route_str not in dirs:
                                dirs[current_route_str] = 0
        case 'dir':
            continue
        case default:
            dirs[current_route_str] += int(line[0])
keys = [x for x in dirs]
keys.sort(reverse=True)
for key in keys: # iterate from longest key, lowest levels
    c = Counter(key)['/']
    for dir in dirs: # check against every dir
        d = Counter(dir)['/']
        if dir[0:len(key)] == key and d == c + 1: # if dir contains key name, goes bottom to top
            dirs[key] += dirs[dir]

sum = 0
for key in dirs:
    if dirs[key] <= 100000:
        sum += dirs[key]
print('pt1:', sum)

max_space = 70000000
unused = max_space - dirs['/']
goal = 30000000 - unused
for w in sorted(dirs, key=dirs.get):
    if dirs[w] > goal:
        print('pt2:', dirs[w], w)
        break



        




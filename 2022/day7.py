f = open('2022/day7input.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    lines.append(line)

dirs = {}
total_lookup = {}
curr_dir = ''
prev_dir = []

for line in lines:
    line = line.split(' ')
    match(line[0]):
        case '$':
            match(line[1]):
                case 'cd':
                    print(' '.join(line))
                    match(line[2]):
                        case '..': # WORKING - THERE ARE DUPE DIRS at different levels
                            curr_dir = prev_dir[len(prev_dir)-1]
                            prev_dir.pop()
                            print(curr_dir)
                        case default: # WORKING
                            if curr_dir:
                                prev_dir.append(curr_dir)
                            curr_dir = line[2]
                            print(curr_dir)
                            if curr_dir not in dirs:
                                dirs[curr_dir] = []
                case 'ls':
                    continue
        case 'dir':
            dirs[curr_dir].append(line[1])
        case default:
            value = int(line[0])
            if curr_dir not in total_lookup:
                total_lookup[curr_dir] = value
            else:
                total_lookup[curr_dir] += value

# TODO go from each level dir

for d in dirs:
    print(d, dirs[d])
sum = 0
for l in total_lookup:
    if total_lookup[l] <= 100000:
        print(l, total_lookup[l])
        sum += total_lookup[l]

print(sum)
f = open('2022/day3input.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    lines.append(line)
def pt1():
    sum = 0
    for line in lines:
        one, two = line[:len(line) // 2], line[len(line) // 2:]
        unique = set(one).intersection(set(two)).pop()
        if 'a'<=unique<='z':
            sum += ord(unique) - 96
        else:
            sum += ord(unique) - 38
    print(sum)

def pt2():
    sum = 0
    sets = [lines[i:i+3] for i in range(0, len(f), 3)]
    for i in sets:
        unique = set(i[0]).intersection(i[1]).intersection(i[2]).pop()
    if 'a'<=unique<='z':
        sum += ord(unique) - 96
    else:
        sum += ord(unique) - 38
    print(sum)
    


    

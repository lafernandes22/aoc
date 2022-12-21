import operator
f = open('2022/day21input.txt', 'r').readlines()

ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
}

def pt1(lines):
    ans_table = {}
    root_index = 0
    for i in range(len(lines)):
        line = lines[i].split(' ')
        lines[i] = line
        if len(line) == 2:
            name = line[0][0:4]
            ans_table[name] = line[1]
        if line[0][0:4] == 'root':
            root_index = i
    
    while len(lines[root_index]) != 2:
        for i in range(len(lines)):
            line = lines[i]
            if len(line) == 4 or len(line) == 5:
                if line[1] in ans_table:
                    lines[i][1] = ans_table[line[1]]
                    lines[i].append('one')
                elif line[3] in ans_table:
                    lines[i][3] = ans_table[line[3]]
                    lines[i].append('two')
            elif len(line) == 6:
                lines[i] = [line[0], ops[line[2]](int(line[1]), int(line[3]))]
                name = line[0][0:4]
                ans_table[name] = lines[i][1]
    print(monkeys[0]+':', ans_table[monkeys[0]])
    print(monkeys[1]+':', ans_table[monkeys[1]])
    print('root:', lines[root_index][1])

monkeys = ('lttc', 'pfjc')
# TODO actually do a search for the number
def pt2():
    root_index = 0
    humn_index = 0
    humn_val = 3093175982590 # BRUTE FORCE I'm TOO TIRED TO MAKE IT ELEGANT
    while True:
        lines = []
        ans_table = {}
        for line in f:
            line = line.replace('\n', '')
            lines.append(line)
        for i in range(len(lines)):
            line = lines[i].split(' ')
            lines[i] = line
            if line[0][0:4] == 'humn':
                humn_index = i
                lines[humn_index][1] = str(humn_val)
            if len(line) == 2:
                name = line[0][0:4]
                ans_table[name] = line[1]
            if line[0][0:4] == 'root':
                root_index = i

        while len(lines[root_index]) != 2:
            for i in range(len(lines)):
                line = lines[i]
                if len(line) == 4 or len(line) == 5:
                    if line[1] in ans_table:
                        lines[i][1] = ans_table[line[1]]
                        lines[i].append('one')
                    elif line[3] in ans_table:
                        lines[i][3] = ans_table[line[3]]
                        lines[i].append('two')
                elif len(line) == 6:
                    lines[i] = [line[0], ops[line[2]](int(line[1]), int(line[3]))]
                    name = line[0][0:4]
                    ans_table[name] = lines[i][1]

        if ans_table[monkeys[0]] == ans_table[monkeys[1]] or ans_table[monkeys[0]] - ans_table[monkeys[1]] < 0:
            print(humn_val)
            print(monkeys[0]+':', ans_table[monkeys[0]])
            print(monkeys[1]+':', ans_table[monkeys[1]])
            break
        print(humn_val, ans_table[monkeys[0]] - ans_table[monkeys[1]])
        humn_val += 1
                    

if __name__ == '__main__':
    lines = []
    for line in f:
        line = line.replace('\n', '')
        lines.append(line)
    pt1(lines)
    pt2()
    
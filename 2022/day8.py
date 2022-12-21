f = open('2022/day8input.txt', 'r').readlines()
lines = []
for line in f:
    line = line.replace('\n', '')
    lines.append(line)

def vis_check(list, pos):
    for i in list:
        if i >= pos:
            return False
    return True

length = len(lines)
width = len(lines[0])

def pt1():
    visible = 0
    for x in range(length):
        if x == 0 or x == length - 1:
            visible += width
            continue
        for y in range(width):
            if y == 0 or y == width - 1:
                visible += 1
            else:
                pos = lines[x][y]
                left, right = [y for y in lines[x][0:y]], [y for y in lines[x][y+1:width]]
                up, down = [x[y] for x in lines[0:x]], [x[y] for x in lines[x+1:length]]
                for i in [left, right, up, down]:
                    i.sort()
                    if vis_check(i, pos):
                        print(i)
                        visible += 1
                        print(x, y, pos)
                        break
    print(visible)

    def pt2():
    best_score = 0
    best_pos = (0,0)
    for x in range(length):
        for y in range(width):
            pos = lines[x][y]
            pos_coord = (x,y)
            left, right = [y for y in lines[x][0:y]], [y for y in lines[x][y+1:width]]
            up, down = [x[y] for x in lines[0:x]], [x[y] for x in lines[x+1:length]]
            left.sort(reverse=True)
            up.sort(reverse=True)
            score = 0
            for view in [left, right, up, down]:
                if not view:
                    continue
                visible = 0
                for tree in view:
                    if tree >= pos:
                        visible += 1
                        break
                    else:
                        visible += 1
                if score == 0:
                    score += visible
                else:
                    score = score * visible
            if score > best_score:
                best_score = score
                best_pos = pos_coord
    print(best_score, best_pos)






            
            

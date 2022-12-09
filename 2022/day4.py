f = open('2022/day4input.txt', 'r').readlines()
lines = []

for line in f:
    line = line.replace('\n', '')
    lines.append(line)

sum = 0
sum2 = 0
for line in lines:
    r1, r2 = line.split(',')
    r1, r2 = r1.split('-'), r2.split('-')
    count = 0 
    for i in range(int(r2[0]), int(r2[1])+1):
        if int(r1[0]) <= i <= int(r1[1]):
            count += 1
    if count == min(int(r1[1])-int(r1[0]), int(r2[1])-int(r2[0]))+1:
        sum += 1
    if count >= 1:
        sum2 += 1
print(sum)
print(sum2)


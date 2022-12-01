with open('2022\day_1_1_input.txt', 'r') as inputs:
    lines = inputs.readlines()
    elves = []
    elf_total = 0
    for line in lines:
        #   the input only shows empty lines on the line before the next elf
        if line.strip() != "":
            elf_total += int(line)
        else:
            elves.append(elf_total)
            elf_total = 0
    elves.sort(reverse=True)
    print(elves[0])
    print(sum(elves[0:3]))
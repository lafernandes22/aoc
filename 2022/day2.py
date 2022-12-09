#   A X Rock    diff 23
#   B Y Paper
#   C Z Scissors
#   A Z
#   B X
#   C Y
with open('2022\day2input.txt', 'r') as inputs:
    lines = inputs.readlines()
    score = 0
    strat_score = 0
    selection = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    beats = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
    value = {
        'X' : 0,
        'Y' : 3,
        'Z' : 6
    }
    
    for line in lines:
        choices = tuple(line.strip('\n').split(' '))
        score += selection[choices[1]]
        if ord(choices[1]) - ord(choices[0]) == 23:
            score += 3
        elif beats[choices[0]] != choices[1]:
            score += 6
    print(score)
    
    for line in lines:
        choices = tuple(line.strip('\n').split(' '))
        strat_score += value[choices[1]]
        match value[choices[1]]:
            case 6:
                match choices[0]:
                    case 'A':
                        strat_score += selection['Y']
                    case 'B':
                        strat_score += selection['Z']
                    case 'C':
                        strat_score += selection['X']

            case 3:
                strat_score += selection[chr(ord(choices[0]) + 23)]
            case 0:
                strat_score += selection[beats[choices[0]]]
    print(strat_score)




        
        
        

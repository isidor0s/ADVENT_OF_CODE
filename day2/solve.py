input = open("input.txt", "r")

opponent = {'A': 1, 'B': 2, 'C': 3}  # mappings
me = {'X': 1, 'Y': 2, 'Z': 3}
lose = {1: 2, 2: 3, 3: 1}  # dictionary of loses
win = {2: 1, 3: 2, 1: 3}  # dictionary of wins

opp = 0
mine = 0
score = 0  # score for part 1
score2 = 0  # score for part 2
while input:
    line = input.readline()
    if (line == ""):  # EOF
        break
    opp = 0
    for key in opponent:  # store value of opponent
        if line[0] == key:
            opp = opponent[key]
    mine = 0
    for key in me:  # store value of my input
        if line[2] == key:
            mine = me[key]

    # first part
    if opp == lose.get(mine):
        score = score + mine
    elif mine == lose.get(opp):
        score = score + mine + 6
    else:
        score = score + mine + 3

    # second part
    if mine == 1:  # need to lose
        score2 = score2 + win.get(opp)
    elif mine == 2:  # need to draw
        score2 = score2 + opp + 3
    else:  # need to win
        score2 = score2 + lose.get(opp) + 6

print(score)
print(score2)


input = open("input.txt", mode='r').read().splitlines()

allPairs = [[[int(i) for i in sec.split('-')] for sec in row.split(',')] for row in input] #split to pairs 

range1 = [range(k[0][0], k[0][1]) for k in allPairs]
range2 = [range(k[1][0], k[1][1]) for k in allPairs]
count = 0
count2 = 0
for i in range(len(range1)):
    # part1
    if range1[i].start <= range2[i].start and range1[i].stop >= range2[i].stop:
        count += 1
    elif range2[i].start <= range1[i].start and range2[i].stop >= range1[i].stop:
        count += 1

     # part 2
    if range1[i].start <= range2[i].stop and range1[i].stop >= range2[i].start:
        count2 += 1
    elif range2[i].start <= range1[i].stop and range2[i].stop >= range1[i].start:
        count2 += 1


print(count)
print(count2)

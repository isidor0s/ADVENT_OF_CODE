input = open("input.txt", "r")

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#zip combines the two lists in one
alphabet = dict(zip(lowercase_letters + uppercase_letters, range(1,53)))
#make a list of zeros as the length of characters 
zeros = [0] * len(lowercase_letters + uppercase_letters)
counter = dict(zip(lowercase_letters + uppercase_letters,zeros))


score = 0
scoreb =0
while input:
    line = input.readline()
    if (line == ""):  # EOF
        break
    part1 = dict(zip(lowercase_letters + uppercase_letters,zeros))
    part2 = dict(zip(lowercase_letters + uppercase_letters,zeros))
    n1 = slice(0,len(line)//2)
    n2 = slice(len(line)//2,len(line))
    first_comp = line[n1]
    second_comp = line[n2]
    for x in first_comp:
        part1[x] +=1
    for x in second_comp:
        if(x!='\n'):
            part2[x] +=1
    for x in alphabet:
        if part1[x]!=0 and part2[x]!=0:
           
            score+= alphabet[x]
            
print(score)
            

    
    
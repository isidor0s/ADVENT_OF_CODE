input = open("input.txt", "r")

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#zip combines the two lists in one
alphabet = dict(zip(lowercase_letters + uppercase_letters, range(1,53)))
#make a list of zeros as the length of characters 
zeros = [0] * len(lowercase_letters + uppercase_letters)
counter = dict(zip(lowercase_letters + uppercase_letters,zeros))


score = 0
count = 0

while input:
    line = input.readline()
   
    if (line == ""):  # EOF
        break
   
    if count == 0:
        line1 = line
        count+=1
            
    elif count ==1:
        line2 = line
        count+=1
    else:
        line3 = line
        count = 0
        part1 = dict(zip(lowercase_letters + uppercase_letters,zeros)) #counts for line 1
        part2 = dict(zip(lowercase_letters + uppercase_letters,zeros)) #counts for line 2
        part3 = dict(zip(lowercase_letters + uppercase_letters,zeros)) #counts for line 3
        for x in line1:
            if(x!='\n'):
                part1[x] +=1
        for x in line2:
            if(x!='\n'):
                part2[x] +=1
        for x in line3:
            if(x!='\n'):
                part3[x] +=1
       
        for x in alphabet:

            if part1[x]!=0 and part2[x]!=0 and part3[x]!=0: #check if it exists in each line 
                print(x,part1[x],part2[x],part3[x]) 
                score+= alphabet[x]
        line1 = ""
        line2 = ""
        line3 = ""
    
        
print(score)





            

    
    
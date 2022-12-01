
input = open("input.txt", "r")


elf_calories = []
count = 0
sum=0

# Loop the input file
while input:
    line = input.readline()
    if(line == ""): #EOF
        break
    if line!="\n":
        count = count + int(line) 
    else:
        elf_calories.append(count) #add to list
        count=0 #reset 
    

elf_calories.append(count)
elf_calories.sort(reverse=True)
sum = elf_calories[0]+elf_calories[1]+elf_calories[2]

print(elf_calories[0])
print(sum)


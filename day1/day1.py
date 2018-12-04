filepath = "./day1/day1.txt"

def inputFileToList(fileName):
    with open(fileName, "r") as inputFile:
        data = inputFile.readlines()
        return(list(map(lambda s: s.replace("\n",""), data)))

def eval(element):
    sign = element[0]
    num = int(element[1:])
    if sign == '+':
        return(num)
    else:
        return(-num)

def sumFrequencyOfFile():
    total = 0
    for elem in inputFileToList(filepath):
        total += eval(elem)
    return(total)

def firstFrequencyHitTwice():
    total = 0
    frequncySet = {0}
    found = False
    while not found:
        for elem in inputFileToList(filepath):
            total += eval(elem)
            if total in frequncySet:
                found = True
                break
            else:
                frequncySet.add(total) 
    return(total)    



print(f"Part 1: {sumFrequencyOfFile()} \n")
print(f"Part 2: {firstFrequencyHitTwice()} \n")
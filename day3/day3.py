filepath = "./day3/day3.txt"

# returns a list of lists (e.g. ["#1", "@", "49,222:", "19x20"])
def input_file_to_list(fileName):
    with open(fileName, "r") as inputFile:
        data = inputFile.readlines()
        return(list(map(lambda s: s.replace("\n","").split(" "), data)))

def overlapping_area():
    #obtain input
    inputList = input_file_to_list(filepath)
    areaDict = dict()

    # iterate over rows
    for row in inputList:
        startx = int(row[2].split(",")[0])
        starty = int(row[2].replace(":","").split(",")[1])
        areax = int(row[3].split("x")[0])
        areay = int(row[3].split("x")[1])

        for xpos in range(startx, areax+startx):
            for ypos in range(starty, areay+starty):
                if (xpos,ypos) in areaDict:
                    areaDict[(xpos,ypos)] += 1
                else:
                    areaDict[(xpos,ypos)] = 1
    return(len(list(filter(lambda x: x > 1, areaDict.values()))))

def intact_area():
    #obtain input
    inputList = input_file_to_list(filepath)
    areaDict = dict()
    allClaims = set()
    destroyedClaims = set()
    # iterate over rows
    for row in inputList:
        claimId = int(row[0].replace("#",""))
        startx = int(row[2].split(",")[0])
        starty = int(row[2].replace(":","").split(",")[1])
        areax = int(row[3].split("x")[0])
        areay = int(row[3].split("x")[1])
        allClaims.add(claimId)

        for xpos in range(startx, areax+startx):
            for ypos in range(starty, areay+starty):
                if (xpos,ypos) in areaDict:
                    destroyedClaims.add(areaDict[(xpos,ypos)])
                    destroyedClaims.add(claimId)
                    areaDict[(xpos,ypos)] = "X"
                else:
                    areaDict[(xpos,ypos)] = claimId

    return(allClaims.difference(destroyedClaims))


print(f"Day 3 Part 1: {overlapping_area()}")
print(f"Day 3 Part 2: {intact_area()}")

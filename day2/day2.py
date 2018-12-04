filepath = "./day2/day2.txt"

def inputFileToList(fileName):
    with open(fileName, "r") as inputFile:
        data = inputFile.readlines()
        return(list(map(lambda s: s.replace("\n",""), data)))

# Function that takes a string and returns a list of letter counts
# Params: s -> a string
# Output -> a list of values
def countDictionary(s):
    tempDict = {}
    for char in s:
        if char in tempDict:
            tempDict[char] += 1
        else:
            tempDict[char] = 1
    # returns a list of values
    return(tempDict.values())

def checkSum():
    twoCounts = 0
    threeCounts = 0
    for elem in inputFileToList(filepath):
        charCountList = countDictionary(elem)
        if 2 in charCountList:
            twoCounts += 1
        if 3 in charCountList:
            threeCounts += 1
    return(twoCounts*threeCounts)

# Function that takes 2 strings and returns a tuple of (Boolean, Int)
# Params: first -> a string, second -> a string
# Output -> Boolean if only 1 difference occured, and an index of last non matching character
def onlyOneDiffInStrings(first, second):
    countDiffs = 0
    indexDiff = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            countDiffs += 1
            indexDiff = i
        if countDiffs > 1: #if more than 1 difference, return immediately
            return(False, indexDiff)
    return(True, indexDiff)

def commonLetters():
    # sort list in alphabetical order
    sortedList = inputFileToList(filepath)
    sortedList.sort()
    
    # loop over each index except last 
    # (assuming there is a solution, last index shouldn't be checked)
    for i in range(len(sortedList)-1):
        keepChecking = True #keep comparing first string against consecutive strings
        counter = 1 # increment to check against consecutive strings
        splitTrack = 0 # keep track of last index where non matching occurs
        while keepChecking:
            diffTuple = onlyOneDiffInStrings(sortedList[i], sortedList[i+counter])
            if diffTuple[0]: # If found only 1 character difference
                split = diffTuple[1]
                return(sortedList[i][0:split] + sortedList[i][split+1:])
            else: # Two strings have more than 1 difference
                if diffTuple[1] < splitTrack: #if strings are getting less similar
                    keepChecking = False
                else: # strings are getting more similar, so keep checking
                    splitTrack = diffTuple[1]    
                    counter += 1


# Part 1 is given a file of random (letters only) strings of equal length
# for each string, if there is exactly 2 matching characters 
# and exactly 3 matching characters
# increment a count for each (but only count once per string per 2 or 3) 
# and return the product of sum of each counts over all input strings
print(f"Part1: {checkSum()} \n")

# Part 2 is given the same input
# find 2 strings that differ by only 1 character
# at the same location
# and return the common letters in order (remove differing character)
print(f"Part2: {commonLetters()} \n")
# given a number, creates a list with that number
# and all numbers to 0, decrement by 1 for each index
def countDown(num):
    newList = []
    for x in range(num, 0, -1):
        newList.append(x)
    return newList

# given a list, prints first index, returns second
def printAndReturn(aList):
    print(aList[0])
    return aList[1]

# given a list, adds first index and list length, returns sum
def firstPlusLength(aList):
    sum = aList[0] + len(aList)
    return sum

# given a list, creates new list with only values greater than 2nd index
def greaterThanSecond(aList):
    newList = []
    if len(aList) < 2:
        return False
    for x in aList:
        if x > aList[1]:
            newList.append(x)
    return len(newList), newList

z = greaterThanSecond([5,1,5])
print(z)

# accepts two integers, size and value
# function creates and returns a list whose length is size and all values are the given value
def thisLengthThatValue(num1,num2):
    newList = []
    for x in range(num1, 0, -1):
        newList.append(num2)
    return newList


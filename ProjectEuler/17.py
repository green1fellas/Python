numbersSingle = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbersTeens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
big = ["hundred", "thousand"]
    
def oneDigit(num):
    num = str(num)
    index = int(num[0:1])
    return str(numbersSingle[index])

def twoDigit(num):
    num = str(num)
    indexSingle = int(num[1:2])
    indexTen = int(num[0:1])
    if(indexTen == 1):
        if(indexSingle == 1):
            return numbersTeens[indexSingle]
        else:
            return numbersTeens[indexSingle]
    else:
        if(indexSingle == 0):
            return tens[indexTen-2]
        else:
            return tens[indexTen-2] + " " + oneDigit(indexSingle)

def threeDigit(num):
    num = str(num)
    indexSingle = int(num[2:3])
    indexTen = int(num[1:2])
    indexHundred = int(num[0:1])

    if(indexSingle == 0 and indexTen == 0):
        return oneDigit(indexHundred) + " hundred"
    elif(indexTen == 0):
        return oneDigit(indexHundred) + " hundred and " + oneDigit(indexSingle)
    else:
        temp = str(indexTen) + str(indexSingle)
        return oneDigit(indexHundred) + " hundred and " + twoDigit(temp)

def fourDigit(num):
    return "one thousand"

def numToString(num):
    num = str(num)
    if(len(num) == 1):
        return oneDigit(num)
    elif(len(num) == 2):
        return twoDigit(num)
    elif(len(num) == 3):
        return threeDigit(num)
    elif(len(num) == 4):
        return fourDigit(num)

def findNumOfLetters(num):
    num = str(num)
    theString = numToString(num)
    count = 0
    for i in range(0, len(theString)):
        if(theString[i:i+1] != " "):
            count += 1
    return count

def main():
    count = 0
    for i in range(1, 1001):
        count += findNumOfLetters(i)

    print(count)

main()
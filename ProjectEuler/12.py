import time
print("Working...")

i = 2
currTriNum = 1
largestNumDiv = 0
while(True):
    # 1 is the first divisor
    numOfDivisors = 1
    if(currTriNum % 20 == 0):
        for j in range(1, int((currTriNum/2) + 1)):
            if(currTriNum % j == 0):
                numOfDivisors = numOfDivisors + 1
    if(numOfDivisors >500):
        print("Answer: " + str(currTriNum))
        print("Number of Divisors: " + str(numOfDivisors))
        break
    if(numOfDivisors > largestNumDiv):
        print("Current Num: " + str(currTriNum))
        print("Divisors: " + str(numOfDivisors))
        print()
        largestNumDiv = numOfDivisors
    currTriNum = currTriNum + i
    i = i + 1


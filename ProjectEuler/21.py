numbers = [0]
sumOfDivisors = [0]
amicablePairA = []
amicablePairB = []

for i in range(1, 10000):
    numbers.append(i)
    divisors = []
    for j in range(1, i):
        if(i % j == 0):
            divisors.append(j)
    result = 0
    for j in range(0, len(divisors)):
        result += divisors[j]
    sumOfDivisors.append(result)

for i in range(1, len(numbers)):
    if(numbers[i] < len(numbers) and sumOfDivisors[numbers[i]] < len(numbers)):
        if(numbers[i] == sumOfDivisors[numbers[sumOfDivisors[numbers[i]]]] and
           sumOfDivisors[numbers[i]] == numbers[sumOfDivisors[numbers[i]]] and
           numbers[i] != sumOfDivisors[numbers[i]] and
           numbers[i] not in amicablePairA and
           numbers[i] not in amicablePairB):
            amicablePairA.append(numbers[i])
            amicablePairB.append(sumOfDivisors[numbers[i]])

result = 0
for i in range(0, len(amicablePairA)):
    result += amicablePairA[i] + amicablePairB[i]
print("Answer: " + str(result))


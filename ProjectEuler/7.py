primeNums = [2, 3]
i = 2
while(len(primeNums) < 5):
    x = False
    for j in range(0, len(primeNums)):
        if(i % primeNums[j] == 0):
            x = True
    if(x == False):
        primeNums.append(i)
    i = i + 1
    # print(len(primeNums))
print(primeNums[len(primeNums)-1])

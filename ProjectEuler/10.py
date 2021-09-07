allNums = [1]*10000000
sum = 0

print("Working...")
for i in range(2, len(allNums)):
    if(allNums[i] == 1):
        sum = sum + i
        for j in range(i, len(allNums), i):
            if(allNums[j] == 1):
                allNums[j] = 0
    if(i == 2000000):
        break
print("Sum: " + str(sum))
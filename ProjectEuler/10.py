allNums = [1]*10000000
sum = 0

for i in range(2, 10):
     for j in range(0, len(allNums), i):
         if(i != j):
            allNums[j] = 0
allNums[1] = 0

for i in range(0, len(allNums)):
    if(allNums[i] == 1):
        sum = sum + i
    if(i < 2000000):
        print(i)
    else:
        break
# print(allNums)
print(sum)

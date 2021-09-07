maxStepsNum = 0
maxSteps = 0

print("working...")
for i in range(1000000, 0, -1):
    num = i
    steps = 0
    while(num != 1):
        steps = steps + 1
        if(num % 2 == 0):
            num = num/2
        else:
            num = (num * 3) + 1
    if(steps > maxSteps):
        maxSteps = steps
        maxStepsNum = i

print(maxStepsNum)
print("Steps: " + str(maxSteps))
    
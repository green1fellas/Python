largest = 0
for i in range(0,1000):
    for j in range(0,1000):
        num = i * j
        num = str(num)
        pal = True
        for l in range(0, len(num)-1):
            if(num[l:l+1] != num[len(num)-(l+1):len(num)-l]):
                pal = False
        if(pal == True):
            num = int(num)
            if(num > largest):
                largest = num
    print("i: " + str(i) + " j: " + str(j))
    print(largest)
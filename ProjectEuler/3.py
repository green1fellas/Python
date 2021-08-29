num = 600851475143
while(True):
    i = 2
    while(True):
        if(num % i == 0):
            num = num / i
            break
        i = i + 1
    print(num)
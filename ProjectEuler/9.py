import math

run = True
for a in range(1, 10000):
    for b in range(1, 10000):
        cSquared = ((a*a) + (b*b))
        c = math.sqrt(cSquared)
        if(c == int(c)):
            if(a + b + c == 1000):
                print(int(a * b * c))
                run = False
                break
    if(run == False):
        break

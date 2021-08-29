import math
smallest = math.inf

def func(num):
    global smallest
    for i in range(20, 10, -1):
        if(num % i == 0):
            func(num / i)
        else:
            return
    if(num < smallest):
        smallest = num

func(670442572800)
print(smallest)
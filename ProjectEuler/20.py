def factorial(num):
    if(num > 1):
        return num * factorial(num-1)
    return 1

def factorialSum(num):
    num = str(num)
    result = 0
    for i in range(0, len(num)-1):
        result += int(num[i:i+1])
    return result

print(factorialSum(factorial(100)))
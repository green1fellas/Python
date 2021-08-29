i = 1
num1 = 1
num2 = 1
result = 0

while(num2 < 4000000):
    if((num1+num2) % 2 == 0):
        result = result + (num1+num2)
    temp = num1
    num1 = num2
    num2 = temp + num2
    i = i+1

print(result)


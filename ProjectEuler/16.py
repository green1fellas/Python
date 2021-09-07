number = pow(2, 1000)
number = str(number)
result = 0

for i in range(0, len(number)):
    result = result + int(number[i:i+1])

print(result)

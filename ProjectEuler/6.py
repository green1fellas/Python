sumOfSquares = 0
squareOfSum = 0

for i in range(1, 101):
    sumOfSquares = sumOfSquares + (i*i)
    squareOfSum = squareOfSum + i

print((squareOfSum * squareOfSum) - sumOfSquares)
f = open("ProjectEuler/18.txt", "r")
triangle = f.read().split("\n")
for i in range(0, len(triangle)):
    triangle[i] = triangle[i].split(' ')

def maxValPath(x, y):
    value = int(triangle[y][x])
    leftPathValue = 0
    rightPathValue = 0
    if(y+1 < len(triangle)):
        leftPathValue = maxValPath(x, y+1)
    if(y+1 < len(triangle) and x+1 < len(triangle[y+1])):
        rightPathValue = maxValPath(x+1, y+1)
    if(leftPathValue > rightPathValue):
        value += leftPathValue
    else:
        value += rightPathValue
    return value

print(maxValPath(0, 0))
def linearTransformation(vector, transformation):
    newVector = [[0],
                 [0]]

    newVector[0][0] = vector[0][0]*transformation[0][0] + vector[1][0]*transformation[0][1]
    newVector[1][0] = vector[0][0]*transformation[1][0] + vector[1][0]*transformation[1][1]

    return newVector

def printMatrix(matrix):

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end="")
        print()

vector = [[2],
          [3]]

transformation = [[1,9],
                  [5,4]]

printMatrix(linearTransformation(vector, transformation))
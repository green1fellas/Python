list = [10,7,9,3,2,1,5,4,6,8]

def sort(left, right):
    if(left < right):
        pivot = partition(left, right)
        sort(left, pivot - 1)
        sort(pivot + 1, right)

def partition(left, right):

    pivot = right
    i = left

    for j in range(left, right):
        if(list[j] < list[pivot]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i = i + 1 
    
    temp = list[i]
    list[i] = list[pivot]
    list[pivot] = temp

    return i


sort(0, len(list) - 1)
print(list)
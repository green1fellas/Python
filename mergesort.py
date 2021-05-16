list = [5,3,6,4,7,2,1,0]

def merge(left, middle, right):

    L = []
    R = []

    for i in range(0, middle-left + 1): #here
        L.append(list[left + i])
    for j in range(0, right - middle): #here
        R.append(list[middle + 1 + j])

    i = 0
    j = 0
    k = left

    while(i < len(L) and j < len(R)):

        if(L[i] <= R[j]): #here
            list[k] = L[i]
            i = i + 1
        else:
            list[k] = R[j]
            j = j + 1

        k = k + 1

    while(i < len(L)):
        list[k] = L[i]
        i = i + 1
        k = k + 1
    
    while(j < len(R)):
        list[k] = R[j]
        j = j + 1
        k = k + 1

def sort(left, right):
    if(left < right):
        middle = int((left + right)/2)
        sort(left, middle)
        sort(middle + 1, right)
        merge(left, middle, right)
        print(list)

sort(0, len(list)-1)
print(list)
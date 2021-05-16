def printLists():
  print(list1)
  print(list2)
  print(list3)
  print()

def move(start, destination):
  if(len(start) != 0):
    destination.append(start.pop())
  printLists()

def fullMove(start, middle, destination):
  move(start, destination)
  move(start, middle)
  move(destination, middle)
  move(start, destination)
  move(middle, start)
  move(middle, destination)
  move(start, destination)
  printLists()

def run(start, middle, destination, num):
  if(num == 3):
    return [start, middle, destination]
  else:
    if(num % 2 == 0):
      fullMove(start, destination, middle)
    else:
      fullMove(start, middle, destination)
    print("num: " + str(num))
    run(start, middle, destination, num-1)
    

list1 = [4,3,2,1]
list2 = []
list3 = []

run(list1, list2, list3, 4)
import queue

class Node:
    leftChild = None
    rightChild = None

    def __init__(self, val):
        self.val = val

class Tree:

    global queue
    queue = queue.Queue()

    root = None

    def insertRec(self, val, temp):

        if(temp is None):
            return Node(val)
        if(val < temp.val):
            temp.leftChild = self.insertRec(val, temp.leftChild)
        elif(val > temp.val):
            temp.rightChild = self.insertRec(val, temp.rightChild)
        elif(val == temp.val):
            return temp
        return temp

    def insert(self, val):
        self.root = self.insertRec(val, self.root)

    def findSmallestNode(self, temp):
        if(temp.leftChild is not None):
            return self.findSmallestNode(temp.leftChild)
        else:
            return temp

    def deleteRec(self, val, temp):
        if(temp is None):
            print(str(val) + " not found.")
        elif(val < temp.val):
            temp.leftChild = self.deleteRec(val, temp.leftChild)
        elif(val > temp.val):
            temp.rightChild = self.deleteRec(val, temp.rightChild)
        elif(val == temp.val):
            if(temp.leftChild is None and temp.rightChild is None):
                return None
            elif(temp.rightChild is None):
                return temp.leftChild
            elif(temp.leftChild is None):
                return temp.rightChild
            else:
                smallestNode = self.findSmallestNode(temp.rightChild)
                temp.val = smallestNode.val
                temp.rightChild = self.deleteRec(smallestNode.val, temp.rightChild)
        return temp

    def delete(self, val):
        self.deleteRec(val, self.root)

    def breadthFirst(self):
        
        queue.put(self.root)

        while(True):
            temp = queue.get()
            if(temp.leftChild is not None):
                queue.put(temp.leftChild)
            if(temp.rightChild is not None):
                queue.put(temp.rightChild)
            print(str(temp.val), "", end="")
            if(queue.empty()):
                break
        print()

    def depthFirst(self):
        self.depthFirstRec(self.root)
        print()

    def depthFirstRec(self, temp):
        if(temp is not None):
            print(str(temp.val), "", end="")
            self.depthFirstRec(temp.leftChild)
            self.depthFirstRec(temp.rightChild)

    def isEmpty(self):
        return self.root is None

    def printTreeRec(self, temp, depth):
        
       if(temp is not None):
            self.printTreeRec(temp.rightChild, depth + 1)
            print("  "*(depth) + str(temp.val))
            self.printTreeRec(temp.leftChild, depth + 1)

    def printTree(self):
        self.printTreeRec(self.root, 0)
    

# Main
tree = Tree()
tree.insert(4)
tree.insert(6)
tree.insert(5)
tree.insert(1)
tree.insert(9)
tree.insert(2)
tree.insert(7)
tree.insert(10)

print("Depth-First:")
tree.depthFirst()

print("Breadth-First, Delete(6):")
tree.delete(6)
tree.breadthFirst()

print("Is empty: " + str(tree.isEmpty()))

print("Print Tree:")
tree.printTree()
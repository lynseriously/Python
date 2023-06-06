class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,newdata): # left < right
        if self.data is not None: # current node
            if newdata < self.data:
                if self.left is None:
                    self.left = Node(newdata)
                else:
                    self.left.insert(newdata) #recurring
            elif newdata > self.data:
                if self.right is None:
                    self.right = Node(newdata)
                else:
                    self.right.insert(newdata) #recurring
        else:
            self.data = newdata
        
    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.data)
        if self.right is not None:
            self.right.traverse()
    
root = Node(30)
root.insert(27)
root.insert(3)
root.insert(37)
root.insert(4)
root.insert(2)
root.insert(28)
root.traverse()

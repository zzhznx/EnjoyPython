class BinarySearchTree(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def find(self, x):
        if x == self.key:
            return self
        elif x < self.key and self.left:
            return self.left.find(x)
        elif x > self.key and self.right:
            return self.right.find(x)
        else:
            return None

    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            return self

    def finMax(self):
        tree = self
        if tree:
            while tree.right:
                tree = tree.right
        return tree

    def insert(self, x):
        if x < self.key:
            if self.left:
                self.left.insert(x)
            else:
                node = BinarySearchTree(x)
                self.left = node
        elif x > self.key:
            if self.right:
                self.right.insert(x)
            else:
                node = BinarySearchTree(x)
                self.right = node

    def delete(self, x):
        if self.find(x):
            if x < self.key:
                self.left = self.left.delete(x)
                return self
            elif x > self.key:
                self.right = self.right.delete(x)
                return self
            else:
                if self.left and self.right:
                    key = self.right.finMin().key
                    self.key = key
                    self.right = self.right.delete(key)
                    return self
                elif self.left:
                    return self.left
                else:
                    return self.right



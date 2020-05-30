class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                newNode = BSTNode(value)
                self.right = newNode
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                newNode = BSTNode(value)
                self.left = newNode

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            return self.left.contains(target) if self.left is not None else False

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            self = self.right
        print(self.value)
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        return None

class Node():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

    def insert(self, item):
        if self.data is None:
            self.data = item
        elif self.left is None and item <= self.data:
            self.left = Node(item)
        elif self.right is None and item > self.data:
            self.right = Node(item)
        elif item <= self.data:
            self.left.insert(item)
        elif item > self.data:
            self.right.insert(item)

    def print_tree(self):
        print self
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()

    def max_depth(self):
        if (self.left is None and self.right is None) or self.data is None :
            return 0
        else:
            l_depth,r_depth = 0,0
            if self.left is not None:
                l_depth = self.left.max_depth()
            if self.right is not None:
                r_depth = self.right.max_depth() 
            return max(l_depth + 1, r_depth + 1)




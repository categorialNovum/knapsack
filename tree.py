import string

class Node():
    def __init__(self,level=0,value=0, capacity=0, estimate=0, parent = None):
#        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.level = level
        self.value = value
        self.capacity = capacity
        self.estimate = estimate

    def __str__(self):
        s = "level : " + str(self.level) + ", value : " + str(self.value) + ", capacity : " + str(self.capacity) + ", estimate : " + str(self.estimate)
        return s

#    def take_item(self, item, path):
#        if not path:
#            self.left = Node(self.level + 1, self.value + item.value, self.capacity - item.weight, self.estimate)
#            return
#        elif path[0] == 1:
#            self.left.take_item(item,path[1:])
#        elif path[0] == 0:
#            self.right.take_item(item,path[1:])

    def take_item(self, item, est):
        self.left = Node(self.level + 1, self.value + item.value, self.capacity - item.weight, est, self)

    def drop_item(self, item, est):
        self.right = Node(self.level +1, self.value, self.capacity, est, self)

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

    def insert_by_key(self, item, keyname):
        if self.data is None:
            self.data = item
        elif self.left is None and getattr(item, keyname) <= getattr(self.data, keyname):
            self.left = Node(item)
        elif self.right is None and getattr(item, keyname) > getattr(self.data, keyname):
            self.right = Node(item)
        elif getattr(item, keyname) <= getattr(self.data, keyname):
            self.left.insert(item)
        elif getattr(item, keyname) > getattr(self.data, keyname):
            self.right.insert(item)

    def print_tree(self):
        print str(self)
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




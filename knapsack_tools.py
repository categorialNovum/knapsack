from operator import attrgetter
from tree import Node

class ks_sort():
    def value_asc(self,items):
        return sorted(items, key=attrgetter('value'))

    def value_desc(self,items):
        return sorted(items, key=attrgetter('value'), reverse=True)

    def weight_asc(self,items):
        return sorted(items, key=attrgetter('weight'))

    def weight_desc(self,items):
        return sorted(items, key=attrgetter('weight'), reverse=True)

    def vw_ratio_asc(self,items):
        return sorted(items, key=attrgetter('vwratio'))

    def vw_ratio_desc(self,items):
        return sorted(items, key=attrgetter('vwratio'), reverse=True)


class estimates():
    #branch and bound requires items be pre-sorted in order of decreasing value/weight ratios
    def optimistic_estimate_presorted(self,items,capacity):
        idx = 0
        estimate = 0
        while capacity > 0 and idx < len(items) :
            if items[idx].weight <= capacity:
                estimate += items[idx].value
                capacity -= items[idx].weight
                idx += 1
            else:
                partial_addition = int((capacity / float(items[idx].weight)) * items[idx].value)
                estimate += partial_addition
                capacity = 0
        return estimate

    def optimistic_estimate_take(self,items,capacity):
        idx = 0
        estimate = 0
        while capacity > 0 and idx < len(items) :
            if items[idx].weight <= capacity:
                estimate += items[idx].value
                capacity -= items[idx].weight
                idx += 1
            else:
                partial_addition = int((capacity / float(items[idx].weight)) * items[idx].value)
                estimate += partial_addition
                capacity = 0
        return estimate

    def optimistic_estimate_drop(self,items,capacity):
        idx = 1
        estimate = 0
        while capacity > 0 and idx < len(items) :
            if items[idx].weight <= capacity:
                estimate += items[idx].value
                capacity -= items[idx].weight
                idx += 1
            else:
                partial_addition = int((capacity / float(items[idx].weight)) * items[idx].value)
                estimate += partial_addition
                capacity = 0
        return estimate

class depth_first_search():
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity
        self.n = len(items)
        self.sorted_items = ks_sort().vw_ratio_desc(items)
        self.bestPath = [self.n]
        self.workingPath = [self.n]
        self.bestProfit = -1
        self.currentProfit
        self.currentWeight
        self.newProfit
        self.newWeight
        self.level

    def __bound(self, currentProfit, currentWeight, currentLevel):
        boundFound = False
        boundVal = -1
        newProfit = currentProfit
        newWeight = currentWeight
        boundLevel = currentLevel + 1
        while (level < self.n and not boundFound):
            # item fits, put it in current solution
            if newWeight + self.items[level].weight <= self.capacity:
                newWeight += items[level].weight
                newProfit += items[level].value
                self.workingPath[boundLevel] = 1
            #item only fits partially, we've hit a boundary. Compute upper bound.
            else:
                boundVal = newProfit + (self.capacity - newWeight) * items[boundLevel].profit / items[boundLevel].weight
                boundFound = True

            if (boundFound):
                #we've hit a wall, try with an item further up the tree
                boundLevel -= 1
                return boundVal
            else
                #profit includes last item
                return newProfit

    def search(self):
        est = estimates()
        estimate = est.optimistic_estimate_presorted(self.sorted_items, self.capacity)
        root = Node(0,0,self.capacity,estimate)
        node = root
        best_profit = -1
        done = False
        print "---------------------------------"
        print "Root ---> " + str(node)
        print self.sorted_items
        print "---------------------------------"
        while not done:
            for i,item in enumerate(self.sorted_items):
                estimate_take = est.optimistic_estimate_take(self.sorted_items[i:], node.capacity)
                estimate_drop = est.optimistic_estimate_drop(self.sorted_items[i:], node.capacity)
                print 'i : ',i
                print item
                print 'capacity : ', node.capacity
                print 'value : ',node.value
                print 'level : ', node.level
#                print 'take : ',estimate_take
#                print 'drop : ',estimate_drop
                #if item.weight <= node.capacity and estimate_take > estimate_drop:
                if item.weight <= node.capacity: 
                    print "taking item"
                    node.take_item(item,estimate_take)
                    node = node.left
                    working_path.append(1)
                else:
                    print "droping item"
                    node.drop_item(item,estimate_drop)
                    node = node.right
                    working_path.append(0)
                print "-----------------"
            done = True
        print "-----------------"
        print working_path
        print "-----------------"
        root.print_tree()

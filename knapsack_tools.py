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
    def __init__(self, items, capacity, bp=-1, cp=0, cw=0, np=0, nw=0, klvl=0, blvl=0):
        self.items = ks_sort().vw_ratio_desc(items)
        self.capacity = capacity
        self.n = len(items)
        self.bestPath = [self.n]
        self.workingPath = [0]*self.n
        self.bestProfit = bp
        self.currentProfit = cp
        self.currentWeight = cw
        self.newProfit = np
        self.newWeight = nw
        self.ksLevel = klvl
        self.boundLevel = blvl

    def printStats(self):
        print '-----------------------------------'
        print 'capcity : ', self.capacity
        print 'workingPath : ', self.workingPath
        print 'bestProfit : ', self.bestProfit
        print 'currentProfit : ', self.currentProfit
        print 'currentWeight : ', self.currentWeight
        print 'newProfit : ', self.newProfit
        print 'newWeight : ', self.newWeight
        print 'ksLevel : ', self.ksLevel
        print 'boundLevel : ', self.boundLevel
        print '-----------------------------------'
        

    def search(self):
        def bound():
            boundFound = False
            boundVal = -1
            self.newProfit = self.currentProfit
            self.newWeight = self.currentWeight
            self.boundLevel = self.ksLevel + 1
            # backtrack until the upper bound is less than the best solution we have
            while (self.boundLevel < self.n and not boundFound):
                # item fits, put it in current solution
                if self.newWeight + self.items[self.boundLevel].weight <= self.capacity:
                    print 'adding ', self.items[self.boundLevel]
                    self.newWeight += self.items[self.boundLevel].weight
                    self.newProfit += self.items[self.boundLevel].value
                    self.workingPath[self.boundLevel] = 1
                #item only fits partially, we've hit a boundary. Compute upper bound.
                else:
                    boundVal = self.newProfit + (self.capacity - self.newWeight) * self.items[self.boundLevel].value / self.items[self.boundLevel].weight
                    boundFound = True

                self.boundLevel += 1
            if (boundFound):
                #we've hit a wall, try with an item further up the tree
                print "wall hit, partial solution : ", boundVal
                self.boundLevel -= 1
                return boundVal
            else:
                print "bound solution hit"
                #profit includes last item
                return self.newProfit

        est = estimates()
        estimate = est.optimistic_estimate_presorted(self.items, self.capacity)
        root = Node(0,0,self.capacity,estimate)
        node = root
        best_profit = -1
        done = False
        print "---------------------------------"
        print "Root ---> " + str(node)
        print self.items
        print "---------------------------------"
        while not done:
            self.printStats()
            while bound() <= self.bestProfit:
                #backtrack while item is not in sack
                while self.ksLevel != 0 and self.workingPath[self.ksLevel] != 1:
                    print 'backtracking'
                    self.ksLevel -= 1
                if self.ksLevel == 0:
                    done = True
                    #return
                else:
                    self.workingPath[self.ksLevel] = 0 # take item out of solution -> branch right
                    self.currentWeight -= self.items[self.ksLevel].weight 
                    self.currentProfit -= self.items[self.ksLevel].value

            self.currentWeight = self.newWeight
            self.currentProfit = self.newProfit
            self.ksLevel = self.boundLevel

            if (self.ksLevel == self.n):
                self.bestProfit = self.currentProfit
                self.bestPath = self.workingPath
                self.ksLevel = self.n -1 
            else:
                self.workingPath[self.ksLevel] = 0

        print "--------------------------------"
        print 'DFS BEST PROFIT : ', self.bestProfit
        print "--------------------------------"


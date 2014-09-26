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
    def search(self,items,capacity):
        sorter = ks_sort()
        est = estimates()
        sorted_items = sorter.vw_ratio_desc(items)
        estimate = est.optimistic_estimate_presorted(sorted_items, capacity)
        root = Node(0,0,capacity,estimate)
        node = root
        path = []
        done = False
        print "---------------------------------"
        print "Root ---> " + str(node)
        print sorted_items
        print "---------------------------------"
        while not done:
            for i,item in enumerate(sorted_items):
                estimate_take = est.optimistic_estimate_take(sorted_items[i:], node.capacity)
                estimate_drop = est.optimistic_estimate_drop(sorted_items[i:], node.capacity)
                print i
                print item
                print 'capacity : ', node.capacity
                print 'value : ',node.value
                print 'take : ',estimate_take
                print 'drop : ',estimate_drop
                if item.weight <= node.capacity and estimate_take > estimate_drop:
                    print "taking item"
                    node.take_item(item,estimate_take)
                    node = node.left
                    path.append(1)
                else:
                    print "droping item"
                    node.drop_item(item,estimate_drop)
                    node = node.right
                    path.append(0)
                if capacity <= 0:
                    break
                print "-----------------"
            done = True
        print path
        root.print_tree()

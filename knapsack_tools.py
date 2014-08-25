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
    def optimistic_estimate_presorted(self,items,capacity):
        idx = 0
        estimate = 0
        while capacity > 0:
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
        path = []
        done = False
        print "---------------------------------"
        print "Root ---> " + str(root)
        print "---------------------------------"
        while not done:
            for item in items:
                if item.weight <= capacity:
                    root.take_item(item,path)
                    capacity -= item.weight
                    path.append(1)
                else:
                    path.append(0)
                if capacity <= 0:
                    break
            done = True
        print path
        root.print_tree()

#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from tree import Node
from knapsack_tools import ks_sort
from knapsack_tools import estimates
from knapsack_tools import depth_first_search
from dynamic_table import dynamic_table
Item = namedtuple("Item", ['index', 'value', 'weight', 'vwratio'])

# easy access to data in repl
def parse_items(file_path):
    input_data_file = open(file_path, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        val = int(parts[0])
        weight = int(parts[1])
        items.append(Item(i-1, val, weight, float(float(val) / float(weight))))
    return items

def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    table = dynamic_table()
    sorter = ks_sort()
    est = estimates()
    dfs = depth_first_search()

    print "# Items : ", str(item_count)
    print "Capacity : ", str(capacity)
    print "--------------------------"

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        val = int(parts[0])
        weight = int(parts[1])
        items.append(Item(i-1, val, weight, float(float(val) / float(weight))))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    #### End basic ####

    dfs.search(items,capacity)

    #root = Node()
    #ratio_items = sorter.vw_ratio_desc(items)
    #estimate = est.optimistic_estimate_presorted(ratio_items,capacity)
    #print root
    #print "--------------------------"
    #print "Estimate : ", str(estimate)
    #print "--------------------------"
    

#    for item in ratio_items:
#        root.insert_by_key(item, "vwratio")

#    root.print_tree()
#    print "--------------------------"
#    print "Depth : ",str(root.max_depth())
#    print "--------------------------"

    table.calculate_solutions(items, capacity)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'


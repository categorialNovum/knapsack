#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from tree import Node
from knapsack_sort import ks_sort
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

    print "# Items : ", str(item_count)
    print "Capacity : ", str(capacity)
    print "--------------------------"

    basic_root = Node()
    vw_root = Node()
    mixed_root = Node()
    ksort = ks_sort()

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        val = int(parts[0])
        weight = int(parts[1])
        items.append(Item(i-1, val, weight, float(float(val) / float(weight))))

    ratio_items = ksort.vw_ratio_desc(items)

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    basic_value = 0
    basic_weight = 0
    basic_taken = [0]*len(items)

    for item in items:
        basic_root.insert(item.value)
        if basic_weight + item.weight <= capacity:
            basic_taken[item.index] = 1
            basic_value += item.value
            basic_weight += item.weight
    #### End basic ####

    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in ratio_items:
        vw_root.insert_by_key(item, 'vwratio')

    for item in items:
        mixed_root.insert_by_key(item, 'vwratio')

    print "BASIC"
    print "----------------"
    basic_root.print_tree()
    print "depth : ",str(basic_root.max_depth())
    print "----------------"
    print "Value / Weight Ratio"
    print "----------------"
    vw_root.print_tree()
    print "depth : ",str(vw_root.max_depth())
    print "----------------"
    print "Mixed"
    print "----------------"
    mixed_root.print_tree()
    print "depth : ",str(mixed_root.max_depth())
    print "----------------"
    
    # prepare the solution in the specified output format
    output_data = str(basic_value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, basic_taken))
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


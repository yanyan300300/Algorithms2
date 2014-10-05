#!/usr/bin/python
import sys

class Item:
    value = 0
    weight = 0

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

#######################################

print "default recursion limit = %d" %sys.getrecursionlimit()

recursion_limit = 10000
print "setting new recursion limit to %d" %recursion_limit
sys.setrecursionlimit(recursion_limit)

test = int(sys.argv[1])

if test:
    infile = sys.argv[2]
else:
    infile ="knapsack_big.txt"

items = []
items.append(Item(0, 0))
with open(infile, "r") as f:
    [knapsack_size, number_of_items] = [int(m) for m in (f.readline().split())]
    for line in f.readlines():
        data_pair = line.split()
        value = int(data_pair[0])
        weight = int(data_pair[1])
        items.append(Item(value, weight))
if test:
    for t in items:
        print t.__dict__
#print knapsack_size
#print number_of_items

#######################################
# initialization

knapsack_optimal_solutions = {}
recursion_num = []
recursion_num.append(0)
def knapsack(item, capacity):
    recursion_num[0] += 1
    if item == 0 or capacity == 0:
        return 0
    elif (item, capacity) in knapsack_optimal_solutions:
        return knapsack_optimal_solutions[(item, capacity)]
    else:
        if capacity-items[item].weight < 0:
            result = knapsack(item-1, capacity)
        else:
            result = max(knapsack(item-1, capacity), knapsack(item-1, capacity-items[item].weight) + items[item].value)
        knapsack_optimal_solutions[(item, capacity)] = result
        return result

print knapsack(number_of_items, knapsack_size)
print "total # of recursions is %d" % recursion_num[0]

f.close()


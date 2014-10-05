#!/usr/bin/python
import sys

#######################################
class Item:
    """ Stores (value, weight) pair"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

#######################################
class Knapsack:
    """ Solves Knapsack problem with recursion and memorization"""

    def __init__(self, infile):
        self.infile = infile
        self.knapsack_optimal_solutions = {}
        self.items = []
        self.items.append(Item(0, 0))
        with open(infile, "r") as f:
            [self.knapsack_size, self.number_of_items] = [int(m) for m in (f.readline().split())]
            for line in f.readlines():
                data_pair = line.split()
                value = int(data_pair[0])
                weight = int(data_pair[1])
                self.items.append(Item(value, weight))
        f.close()
        if test:
            for t in self.items:
                print t.__dict__

    def solve_knapsack(self, item, capacity):
        if item == 0 or capacity == 0:
            return 0
        elif (item, capacity) in self.knapsack_optimal_solutions:
            return self.knapsack_optimal_solutions[(item, capacity)]
        else:
            if capacity-self.items[item].weight < 0:
                result = self.solve_knapsack(item-1, capacity)
            else:
                result = max(self.solve_knapsack(item-1, capacity), self.solve_knapsack(item-1, capacity-self.items[item].weight) + self.items[item].value)
            self.knapsack_optimal_solutions[(item, capacity)] = result
            return result



#######################################

print "default recursion limit = %d" %sys.getrecursionlimit()

recursion_limit = 10000
print "setting new recursion limit o %d" %recursion_limit
sys.setrecursionlimit(recursion_limit)

test = int(sys.argv[1])

if test:
    infile = sys.argv[2]
else:
    infile ="knapsack_big.txt"

ks = Knapsack(infile)

print ks.solve_knapsack(ks.number_of_items, ks.knapsack_size)


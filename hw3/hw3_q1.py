#!/usr/bin/python
import sys

class Item:
    value = 0
    weight = 0

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

#######################################

test = int(sys.argv[1])

if test:
    infile = sys.argv[2]
else:
    infile ="knapsack1.txt"

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
A = [[0 for x in range(knapsack_size+1)] for i in range(number_of_items+1)]
if test:
    print A
for i in range(1, number_of_items+1):
    for x in range(0, knapsack_size+1):
        if x-items[i].weight < 0:
            A[i][x] = A[i-1][x]
        else:
            A[i][x] = max(A[i-1][x], A[i-1][x-items[i].weight] + items[i].value)

if test:
    for i in range(0, number_of_items+1):
        print A[i]
print "the maximum value is %d" % A[number_of_items][knapsack_size]

f.close()


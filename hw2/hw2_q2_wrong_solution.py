#!/usr/bin/python
import sys
from union_find import union_find

def distance_less_than_3(bits, bits_num):
    result = []
    # compute distance 1
    for i in range(0, bits_num):
        result.append(bits ^ (1 << i)) 
    # compute distance 2
    for i in range(0, bits_num):
        for j in range(i+1, bits_num):
            result.append(bits ^ ((1 << i) | (1 << j))) 
    result.sort()
    return result

def find_in_ascending_list(inlist, item):
    for i in inlist:
        if item == i:
            return True
        elif item < i:
            return False
    return False

test = int(sys.argv[1])
if test:
    infile = "clustering_big_simple.txt"
else:
    infile ="clustering_big.txt"

nodes = []

with open(infile, "r") as f:
    first_line = f.readline().split()
    node_num = int(first_line[0])
    bit_num = int(first_line[1])
    for line in f.readlines():
        #nodes.append([int(m) for m in line.split()])
        nodes.append(int(line.strip().replace(" ", ""), 2))

if test:
    print node_num
    print bit_num
    print nodes

nodes_union = union_find(node_num)

clusters = node_num

for n in range(1, node_num+1):
    all_neighbors = distance_less_than_3(nodes[n-1], bit_num)
    for m in range(n+1, node_num+1):
        if nodes_union.find(n) != nodes_union.find(m):
            if find_in_ascending_list(all_neighbors, nodes[m-1]):
                nodes_union.union(n, m)
                clusters -= 1

print "maximum k is %d" %clusters
f.close()


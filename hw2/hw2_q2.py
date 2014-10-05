#!/usr/bin/python
import sys
from union_find import union_find

def distance_less_than_3(bits, bits_num):
    result = []
    # compute distance 1
    result.append(bits)
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

nodes = {}
duplicate_node_count = 0
with open(infile, "r") as f:
    first_line = f.readline().split()
    node_num = int(first_line[0])
    bit_num = int(first_line[1])
    iter = 0
    for line in f.readlines():
        iter += 1
        key = int(line.strip().replace(" ", ""), 2)
        if key in nodes:
            duplicate_node_count += 1
        else:
            nodes[key]= iter

if test:
    print node_num
    print bit_num
    print nodes
    a = []
    for key, n in nodes.iteritems():
        a.append(key)
    print sorted(a)
    for key1, n1 in nodes.iteritems():
        for key2, n2 in nodes.iteritems():
            if n1 != n2:
                xor = key1 ^ key2
                i = 0
                sum = 0
                while i != bit_num:
                    sum += (xor & (1<<i))>>i
                    i += 1
                if sum < 3:
                    print "%d & %d, dis=%d" %(n1, n2, sum)



nodes_union = union_find(node_num)

clusters = node_num

#for n in range(1, node_num+1):
for key, n in nodes.iteritems():
    if test:
        print "key:node %d %d" %(key, n)
    all_neighbors = distance_less_than_3(key, bit_num)
    for neighbor in all_neighbors:
        if (neighbor in nodes):
            neighbor_node = nodes[neighbor];
            if nodes_union.find(n) != nodes_union.find(neighbor_node):
                if test:
                    print "merging %d and %d" %(n, neighbor_node)
                nodes_union.union(n, neighbor_node)
                clusters -= 1
clusters -= duplicate_node_count
print "maximum k is %d" %clusters
f.close()


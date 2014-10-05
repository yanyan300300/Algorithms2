#!/usr/bin/python
import sys
from union_find import union_find

class Edge:
    cost = 0
    node1 = 0
    node2 = 0

    def __init__(self, node1, node2, cost):
        self.cost = cost
        self.node1 = node1
        self.node2 = node2

edges = []
test = int(sys.argv[1])

if test:
    infile = sys.argv[2]
else:
    infile ="clustering1.txt"
with open(infile, "r") as f:
    num = int(f.readline().strip())
    for line in f.readlines():
        data = line.split()
        node1 = int(data[0])
        node2 = int(data[1])
        cost = int(data[2])
        edges.append(Edge(node1, node2, cost))


# sort edges based on edge.cost
# if test:
#   for e in edges:
#       print e.__dict__

edges_sorted = sorted(edges, key=lambda e: e.cost)

#print edges_sorted[0].__dict__
#print edges_sorted[1].__dict__
if test:
   for e in edges_sorted:
       print e.__dict__


nodes = union_find(num)

cluster = num

for e in edges_sorted:
    if cluster > 4:
        if nodes.find(e.node1) != nodes.find(e.node2):
            if test:
                print "merging %d and %d" %(e.node1, e.node2)
                print "node %d's head is %d, node %d's head is %d" %(e.node1, nodes.find(e.node1), e.node2, nodes.find(e.node2))
            nodes.union(e.node1, e.node2)
            cluster -= 1
    else:
        if nodes.find(e.node1) != nodes.find(e.node2): 
            print "minimum spacing is %d" %e.cost
            break

f.close()


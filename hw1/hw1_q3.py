from pqdict import PQDict
test = 0
edges = []
if test:
    infile = "edges_simple.txt"
    #infile = "edges.txt"
else:
    infile = "edges.txt"
with open(infile,"r") as f:
    l = f.readline().split(); 
    n = int(l[0])
    m = int(l[1])
    for line in f.readlines():
        edges.append([int(num) for num in line.split()])
print "n = %d" %n
print "m = %d" %m

# Initialize
mst = []
mst.append(edges[0][0])
# costs
costs = [1000000]*(n+1)
# find the key for each node
if test:
    print "edges are", edges
for edge in edges:
  node1 = edge[0]
  node2 = edge[1]
  cost = edge[2]
  if node1 == mst[0]:
      if costs[node2] > cost:
          costs[node2] = cost
  elif node2 == mst[0]:
      if costs[node1] > cost:
          costs[node1] = cost
if test:
    print "initial costs is", costs
    
# insert node to heap
heap = PQDict()
for node in range(2,n+1):
    heap.additem(node, costs[node])
if test:
    print "heap is", heap
cost_sum = 0
while len(heap) != 0:
    next_node = heap.popitem(); # (node, cost)
    if test:
        print "next_node is %d" % next_node[0]
    cost_sum = cost_sum + next_node[1]
    if test:
        print "current cost_sum is %d" % cost_sum
    mst.append(next_node[0])
    if test:
        print "current mst is", mst
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        cost = edge[2]
        if (node1 == next_node[0]) and (node2 not in mst):
            if costs[node2] > cost:
                if test:
                    print "node %d needs update, old cost is %d, new cost is %d" % (node2, costs[node2], cost)
                heap.updateitem(node2, cost)
                costs[node2] = cost
        elif (node2 == next_node[0]) and (node1 not in mst):
            if costs[node1] > cost:
                if test:
                    print "node %d needs update, old cost is %d, new cost is %d" % (node1, costs[node1], cost)
                heap.updateitem(node1, cost)
                costs[node1] = cost

if test:
    print "the mst is", mst
    print "mst size is %d" % len(mst)
print "the total cost is %d" %cost_sum
f.close()

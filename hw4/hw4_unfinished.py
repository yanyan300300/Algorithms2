#!/usr/bin/python
import sys

#######################################
class Edge:
    """ Stores an edge with tail, head and length"""
    def __init__(self, tail, head, length):
        self.tail = tail
        self.head = head
        self.length = length

#######################################
class APSP:
    """Find the All-Pairs Shortest Paths of a graph. Reports if there is any negtive-cost cycle"""

    def __init__(self, infile):
        self.infile = infile
        self.edges = []
        #self.edges.append(Item(0, 0))
        with open(infile, "r") as f:
            [self.vertice_num, self.edge_num] = [int(m) for m in (f.readline().split())]
            for line in f.readlines():
                edge_data = line.split()
                self.edges.append(Edge(int(edge_data[0]), int(edge_data[1]), int(edge_data[2])));
        f.close()
        if test:
            for t in self.edges:
                print t.__dict__
"""
    def johnson(self):
        # Add a new vertex s = self.vertice_num + 1
        for i in range(1, self.vertice_num + 1):
            self.edges.append(Edge(self.vertice_num + 1, i, 0)
        # Run Bellman-Ford for s -> rest of vertices
        shortest_length_from_s = self.bellman_ford(self, self.vertice_num + 1, self.vertice_num + 1)
"""        



    def bellman_ford(self, vertice_num, source):
        # Initialize
        for j in range(0, vertice_num + 1): 
            if j == source:
                optimal[0][j] = 0
            else
                optimal[0][j] = 10000
        # Solve sub-problem
        for i in range(1, vertice_num + 1):
            for j in range(1, vertice_num + 1):
                optimal[i][j] = min(optimal[i-1][j], 
                    

        # Detecting negtive cycle

        return optimal



    def floyd_warshall(self):
        # Initialize
        sub_problem_solution = [[[10000 for k in range(self.vertice_num+1)] for j in range(self.vertice_num+1)] for i in range(self.vertice_num+1)]
        for i in range(1, self.vertice_num+1):
            sub_problem_solution[i][i][0] = 0
        for edge in self.edges:
            sub_problem_solution[edge.tail][edge.head][0] = edge.length
        if test:
            print sub_problem_solution

        # Solve problem
        for k in range(1, self.vertice_num+1):
            for i in range(1, self.vertice_num+1):
                for j in range(1, self.vertice_num+1):
                    sub_problem_solution[i][j][k] = \
                        min(sub_problem_solution[i][j][k-1], sub_problem_solution[i][k][k-1] + sub_problem_solution[k][j][k-1])
        
        # Detect negtive cycle
        for i in range(1, self.vertice_num+1):
            if sub_problem_solution[i][i][self.vertice_num] < 0:
                return "NULL"

        # Find shortest path
        shortest_path = 10000;
        for i in range(1, self.vertice_num+1):
            for j in range(1, self.vertice_num+1):
                if sub_problem_solution[i][j][self.vertice_num] < shortest_path:
                    shortest_path = sub_problem_solution[i][j][self.vertice_num]
        return shortest_path


#######################################


test = int(sys.argv[1])

infile = sys.argv[2]

my_apsp = APSP(infile)

print my_apsp.floyd_warshall() 


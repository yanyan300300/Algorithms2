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

    def floyd_warshall(self):
        # Initialize
        sub_problem_solution = [[[10000 for k in range(0,2)] for j in range(self.vertice_num+1)] for i in range(self.vertice_num+1)]
        for i in range(1, self.vertice_num+1):
            sub_problem_solution[i][i][0] = 0
        for edge in self.edges:
            sub_problem_solution[edge.tail][edge.head][0] = edge.length

        # Solve problem
        for k in range(1, self.vertice_num+1):
            for i in range(1, self.vertice_num+1):
                for j in range(1, self.vertice_num+1):
                    if (k % 2 == 1):
                        sub_problem_solution[i][j][1] = \
                            min(sub_problem_solution[i][j][0], sub_problem_solution[i][k][0] + sub_problem_solution[k][j][0])
                    else:
                        sub_problem_solution[i][j][0] = \
                            min(sub_problem_solution[i][j][1], sub_problem_solution[i][k][1] + sub_problem_solution[k][j][1])

        
        # Detect negtive cycle
        for i in range(1, self.vertice_num+1):
            if (self.vertice_num % 2 == 0) and (sub_problem_solution[i][i][0] < 0):
                return "NULL"
            elif (self.vertice_num % 2 == 1) and (sub_problem_solution[i][i][1] < 0):
                return "NULL"

        # Find shortest path
        shortest_path = 10000;
        for i in range(1, self.vertice_num+1):
            for j in range(1, self.vertice_num+1):
                if (self.vertice_num % 2 == 0):
                    if (i != j) and (sub_problem_solution[i][j][0] < shortest_path):
                        shortest_path = sub_problem_solution[i][j][0]
                else:
                    if (i != j) and (sub_problem_solution[i][j][1] < shortest_path):
                        shortest_path = sub_problem_solution[i][j][1]

        return shortest_path


#######################################


test = int(sys.argv[1])

infile = sys.argv[2]

my_apsp = APSP(infile)

print my_apsp.floyd_warshall() 


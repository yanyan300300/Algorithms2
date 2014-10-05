#!/usr/bin/python
import sys
#######################################
class TwoSAT:

    def __init__(self, infile):
        self.infile = infile
        # Construct implication graph
        # self.vertices[0] = x1
        # self.vertices[0 + self.total_vertices] = x1'
        self.vertices = []
        with open(infile, "r") as f:
            self.total_vertices = int(f.readline().split()[0])
            self.vertices = [ [] for i in range(self.total_vertices*2)]
            for line in f.readlines():
                data = line.split()
                a = int(data[0])
                b = int(data[1])
                if a < 0 and b > 0:
                    self.vertices[-a-1].append(b-1)
                    self.vertices[b-1 + self.total_vertices].append(-a-1 + self.total_vertices)
                elif a < 0 and b < 0:
                    self.vertices[-a-1].append(-b-1 + self.total_vertices)
                    self.vertices[-b-1].append(-a-1 + self.total_vertices)
                elif a > 0 and b > 0:
                    self.vertices[a-1 + self.total_vertices].append(b-1)
                    self.vertices[b-1 + self.total_vertices].append(a-1)
                else:   # a > 0 and b < 0
                    self.vertices[a-1 + self.total_vertices].append(-b-1 + self.total_vertices)
                    self.vertices[-b-1].append(a-1)
        f.close()

        self.t = 0  # number of vertices that have been fully explored
        self.s = -1 # the vertex from which the last DFS call was invoked
        self.explored = []

        #print self.total_vertices
        #print self.vertices

    def solve(self):
        if self.scc(self.vertices):
            return "NOSAT"
        else:
            return "SAT"

    def scc(self, graph):
        """Use Tarjan's algorithm to find the SCC. graph is the adjacency list representation"""
        found = False
        # Reverse the graph
        graph_reversed = [ [] for i in range(len(graph))]
        for i in range(len(graph)):
            for vertex in graph[i]:
                graph_reversed[vertex].append(i)
        #print graph_reversed
        # p[i] is the corresponding vertex with finish time i
        p = [-1 for i in range(len(graph_reversed)+1)]
        # leaders stores the DFS leader of each vertex of graph with sequence f
        leaders = [-1 for i in range(len(graph))]

        seq = []
        for i in range(0, len(graph_reversed)+1):
            seq.append(i-1)

        self.dfs_loop(graph_reversed, seq, p, [])
        self.dfs_loop(graph, p, [], leaders)
        #print leaders
        # Find if there are any vertices share a common leader
        for i in range(0, len(leaders)/2):
            if leaders[i] == leaders[i+len(leaders)/2]:
                found = True
                break
        return found

    def dfs_loop(self, graph, seq, p, leaders):
        """DFS graph. Seq is an array deciding the traverse sequence. Leaders is an array records the
        leader of each vertex"""
        self.t = 0   # reset
        self.s = -1  # reset
        self.explored = [False for i in range(len(graph))]   # reset
        for i in range(len(seq)-1, 0, -1):    # Decreasing order
            if not self.explored[seq[i]]:
                self.s = seq[i]
                self.dfs(graph, seq[i], p, leaders)

    def dfs(self, graph, i, p, leaders):
        """DFS graph from vertex i"""
        self.explored[i] = True
        if leaders:
            leaders[i] = self.s
        for j in graph[i]: # TODO: seq!
            if not self.explored[j]:
                self.dfs(graph, j, p, leaders)
        self.t += 1
        if p:
            p[self.t] = i





#######################################

if __name__ == '__main__':
    my_2sat = TwoSAT("2sat6.txt")
    print my_2sat.solve()


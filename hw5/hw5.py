#!/usr/bin/python
import sys
import math
import heapq
#######################################
class Vertex:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
#######################################
class TSP:

    def __init__(self, infile):
        self.infile = infile
        self.vertices = []
        with open(infile, "r") as f:
            self.total_vertices = int(f.readline().split()[0])
            i = 0
            for line in f.readlines():
                data = line.split()
                self.vertices.append(Vertex(i, float(data[0]), float(data[1])))
                i += 1
        f.close()
        # Stores calculated distance between two vertices
        # TODO: don't need that much due to [v_min][v_max]
        self.distance = [[-1 for i in range(self.total_vertices)] for j in range(self.total_vertices)]
        print self.total_vertices
        for t in self.vertices:
            print t.__dict__

    def cal_distance(self, vertex1, vertex2):
        """ """
        v_min = min(vertex1, vertex2)
        v_max = max(vertex1, vertex2)
        # Has been calculated before
        if self.distance[v_min][v_max] != -1:
            return self.distance[v_min][v_max]
        elif v_min == v_max:
            result = 0
        else:
            result = math.sqrt((self.vertices[vertex1].x-self.vertices[vertex2].x) ** 2 + (self.vertices[vertex1].y-self.vertices[vertex2].y) ** 2)
        self.distance[v_min][v_max] = result
        return result

    def solve(self):
        mid_points_left = {}
        mid_points_right = {}
        #for i in range(0, 4):
        for i in range(0, 2):
            mid_points_left[i] = 1
        #for i in range(6, 7):
         #   mid_points_right[i] = 1
        #return self.find_shortest_path(4, 5, mid_points_left) + self.find_shortest_path(4, 5, mid_points_right)
        return self.find_shortest_path(2, 3, mid_points_left) + self.find_shortest_path(2, 3, mid_points_right)

    
    def find_shortest_path(self, start, end, mid_points):
        """ Find the shortest path from start to end and must travel via all mid_points """
        min_p = 100000
        v_dict = {}
        for v in mid_points:
            # mask the current items
            if mid_points[v] == 1:
                mid_points[v] = 0
                last_hop_distance = self.cal_distance(v, end)
                f_result = self.find_shortest_path(start, v, mid_points) + last_hop_distance
                int_result = int(f_result)
                v_dict[int_result] = v
                if f_result < min_p:
                    min_p = f_result
                #heapq.heappush(h, (self.find_shortest_path(start, v, mid_points) + last_hop_distance))
                #heapq.heappush(h, f_result)
                mid_points[v] = 1
        # Base case: when all items in mid_point are masked out  
        #if not h:
        if min_p == 100000:
            shortest_path = self.cal_distance(start, end)
        else:
            #shortest_path = heapq.heappop(h)
            shortest_path = min_p
            print "%d %f %d" %(end, shortest_path, v_dict[int(shortest_path)])
            print mid_points
        return shortest_path
#######################################

if __name__ == '__main__':
    my_tsp = TSP("tsc_test2.txt")

    print my_tsp.solve()


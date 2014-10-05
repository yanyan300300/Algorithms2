class union_find:
    """union_find data structure stores nodes and their belonging unions"""
    # head stores the head node of the node of index
    head = []
    # size stores the count of the nodes whose head is the node of index
    size = []
    # num is the total number of the nodes
    num = 0

    def __init__(self, num):
        self.num = num
        for i in range (0, num):
            self.head.append(i)
            self.size.append(1)
    # find which union the input node is in
    # union is identified with the "true head node"
    # "true head node" is defined as its head is itself
    def find(self, node):
        if node > self.num:
            print "node %d does not exits!" %node
            return 0
        current_node = node-1
        next_node = self.head[current_node]
        while not next_node == current_node:
            current_node = next_node
            next_node = self.head[current_node]
        return current_node+1

    def union(self, node1, node2):
        if node1 > self.num or node2 > self.num:
            print "node(s) does not exits!"
            return
        head1 = self.find(node1)-1
        head2 = self.find(node2)-1
        size1 = self.size[head1]
        size2 = self.size[head2]
        if False:
            print "head1 %d, head2 %d, size1 %d, size2 %d" %(head1, head2, size1, size2)
        if size1 < size2:
            self.head[head1] = self.head[head2]
            self.size[head2] = self.size[head1] + self.size[head2]
        else:
            self.head[head2] = self.head[head1]
            self.size[head1] = self.size[head1] + self.size[head2]
        return

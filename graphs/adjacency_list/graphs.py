from Queue import Queue

class Graph(object):

    class Item(object):
        def __init__(self, d, w):
            self.destination = d
            self.weight = w

    def __init__(self):        
        self.initial_size = 2
        self.adj = [[] for _ in range(self.initial_size)]

    def add_edge(self, source, destination, weight):
        required_size = max(source, destination) + 1

        if len(self.adj) < required_size:
            new_list = [[] for _ in range(required_size)]

            for i in range(len(self.adj)):
                new_list[i] = self.adj[i]

            self.adj = new_list

        self.adj[source].append(self.Item(destination, weight))
        self.adj[destination].append(self.Item(source, weight))

    def get_vertex_count(self):
        return len(self.adj)

    def explore(self, vertex, visited):
        visited[vertex] = True
        print str(vertex)

        for neighbor in self.adj[vertex]:
            if not visited[neighbor.destination]:
                self.explore(neighbor.destination, visited)

    def DFS(self):
        print "DFS"

        # for all v belonging to V, mark as unvisited
        visited = [False for _ in range(len(self.adj))]

        for vertex in range(len(self.adj)):
            if not visited[vertex]:
                self.explore(vertex, visited)

    def BFS(self):
        print "BFS"

        dist = [-1 for _ in range(len(self.adj))]
        prev = [-1 for _ in range(len(self.adj))]

        dist[0] = 0

        q = Queue()

        q.put(0)

        while not q.empty():
            vertex = q.get()

            for neighbor in self.adj[vertex]:
                
                if dist[neighbor.destination] == -1:
                    q.put(neighbor.destination)
                    dist[neighbor.destination] = dist[vertex] + 1
                    prev[neighbor.destination] = vertex

        print "Distances and previous"
        for vertex in range(len(self.adj)):
            print "Vertex " + str(vertex) + ": " + str(dist[vertex]) + " - Previous: " + str(prev[vertex])

    def count_components(self):
        visited = [False for _ in range(len(self.adj))]

        cc = 0

        for vertex in range(len(self.adj)):
            if not visited[vertex]:
                cc += 1
                self.explore(vertex, visited)

        return cc

    def print_debug(self):
        print "Adjacency List"
        print "Vertices: " + str(self.get_vertex_count()) + "\n"

        for vertex in range(len(self.adj)):
            print "Vertex " + str(vertex) + ":",

            for neighbor in self.adj[vertex]:
                print " " + str(neighbor.destination),
           
            print ""

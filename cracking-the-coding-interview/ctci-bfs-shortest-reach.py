class Graph:
    def __init__(self, node_count):
        self.nodes = range(node_count)
        self.neighbors = { node: [] for node in self.nodes }
    
    def connect(self, a, b):
        self.neighbors[a] = self.neighbors.get(a, []) + [b]
        self.neighbors[b] = self.neighbors.get(b, []) + [a]

    def find_all_distances(self, start_node):
        visited = { start_node: 0 }
        queue = [start_node]
        while len(queue):
            current = queue.pop()
            cost = visited[current]
            for neighbor in self.neighbors[current]:
                if neighbor not in visited or visited[neighbor] > cost + 6:
                    visited[neighbor] = cost + 6
                    queue.append(neighbor)
        
        other_nodes = [node for node in self.nodes if node != start_node]
        return map(lambda node: visited[node] if node in visited else -1, other_nodes)


query_count = input()
for i in range(query_count):
    node_count, edge_count = map(int, raw_input().split())
    graph = Graph(node_count)
    for i in xrange(edge_count):
        x, y = map(int, raw_input().split())
        graph.connect(x - 1, y - 1) 
    s = input()
    print " ".join(map(str, graph.find_all_distances(s - 1)))
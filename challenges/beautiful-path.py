import sys
from Queue import PriorityQueue

class Parser:
    def parse(self, input):
        lines_values = [tuple(map(int, line.split())) for line in input]
        (node_count, edge_count) = lines_values[0]
        (start_node, end_node) = lines_values[-1]
        return (node_count, edge_count, start_node, end_node, lines_values[1:-1])

class BeautifulPath:
    def __init__(self, edges):
        self.node_edges_map = {}
        for (a, b, cost) in edges:
            self.add_directed_edge(a, b, cost)
            self.add_directed_edge(b, a, cost)
    
    def add_directed_edge(self, frm, to, cost):
        self.node_edges_map[frm] = self.node_edges_map.get(frm, [])
        self.node_edges_map[frm].append((to, cost))

    def find_least(self, start_node, end_node):
        visited = {}
        queue = PriorityQueue()
        queue.put((0, start_node))
        while not queue.empty():
            (running_cost, current_node) = queue.get()
            if current_node == end_node:
                return running_cost
            for (next_node, cost) in self.node_edges_map.get(current_node, []):
                new_running_cost = running_cost | cost
                if next_node in visited and new_running_cost >= visited[next_node]:
                    continue  # seen it before cheaper
                visited[next_node] = new_running_cost
                queue.put((new_running_cost, next_node))
        return -1

(node_count, edge_count, start_node, end_node, edges) = Parser().parse(sys.stdin)

print BeautifulPath(edges).find_least(start_node, end_node)
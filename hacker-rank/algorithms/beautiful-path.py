import sys
import time
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
        lowest_end_cost = None
        visited = {}
        queue = PriorityQueue()
        queue.put((0, start_node))
        while not queue.empty():
            (running_cost, current_node) = queue.get()
            for (next_node, cost) in self.node_edges_map.get(current_node, []):
                new_running_cost = running_cost | cost
                visited_key = "{}.{}".format(next_node, new_running_cost)
                if visited_key in visited and new_running_cost >= visited[visited_key]:
                    continue  # seen it before cheaper
                if lowest_end_cost is not None and running_cost >= lowest_end_cost:
                    continue  # wont get cheaper than something aleady found
                if next_node == end_node and (new_running_cost < lowest_end_cost or lowest_end_cost is None):
                    lowest_end_cost = new_running_cost
                visited[visited_key] = new_running_cost
                queue.put((new_running_cost, next_node))
        return lowest_end_cost if lowest_end_cost is not None else -1

(node_count, edge_count, start_node, end_node, edges) = Parser().parse(sys.stdin)

start = time.time()
print BeautifulPath(edges).find_least(start_node, end_node)
end = time.time()
print >> sys.stderr, "Took time: {}".format(end - start)
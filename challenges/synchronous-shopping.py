import sys
import time
from Queue import PriorityQueue


class Parser:
    def process_header(self, tokens):
        total_shops = tokens[0]
        all_fishies = (2 ** tokens[2]) - 1
        return (total_shops, all_fishies)

    def parse(self, input):
        total_shops = all_fishies = shop_fishies = shop_roads = last_id = None
        for idx, line in enumerate(input):
            tokens = map(int, line.split())
            if idx == 0: # get the number of shops and the different types of fish
                (total_shops, all_fishies) = self.process_header(tokens)
                shop_fishies = [0] * total_shops
                shop_roads = {n: [] for n in range(0, total_shops)}
            elif idx <= len(shop_fishies): # get fish types for each shop and bitpack them
                shop_id = idx - 1
                for col in range(1, tokens[0] + 1):
                    shop_fishies[shop_id] |= 2 ** (tokens[col] - 1)
            else: # grab the road destinations and the road cost
                shop_roads[tokens[0] - 1].append((tokens[1] - 1, tokens[2]))
                shop_roads[tokens[1] - 1].append((tokens[0] - 1, tokens[2]))

        return (total_shops, all_fishies, shop_fishies, shop_roads, 0, total_shops - 1)


class SyncShopper:

    def findLeast(self, all_fishies, shop_fishies, shop_roads, first_id, last_id):
        terminal_seen = 0
        terminal_fishies = {} # key is fish mask, value is cost
        visited = {}

        queue = PriorityQueue()
        queue.put((0, first_id, shop_fishies[first_id]))
        
        while not queue.empty():
            (running_cost, shop_id, seen_fish) = queue.get()
            if shop_id == last_id and seen_fish != 0:
                #print >> sys.stderr, ">! Got to {} at cost {} with fish {}".format(shop_id, running_cost, seen_fish)
                terminal_fishies[seen_fish] = terminal_fishies.get(seen_fish, running_cost)
                terminal_seen |= seen_fish
                if terminal_seen == all_fishies:
                    for terminal_fish in terminal_fishies:
                        if all_fishies == terminal_fish | seen_fish:
                            print >> sys.stderr, "Found combination: (Fish:{},Cost:{}) with (Fish:{},Cost:{})".format(seen_fish, running_cost, terminal_fish, terminal_fishies[terminal_fish])
                            return max(running_cost, terminal_fishies[terminal_fish])

            for (neighbor,road_cost) in shop_roads[shop_id]:
                new_seen_fish = seen_fish | shop_fishies[neighbor]
                new_running_cost = running_cost + road_cost

                visited_key = "{}.{}".format(neighbor, new_seen_fish)
                if visited_key in visited and new_running_cost >= visited[visited_key]:
                    continue # seen it cheaper so skip

                visited[visited_key] = new_running_cost
                queue.put((new_running_cost, neighbor, new_seen_fish))

(total_shops, all_fishies, shop_fishies, shop_roads, first_id, last_id) = Parser().parse(sys.stdin)
print >> sys.stderr, "First: {}, Last: {}, All Fish: {}".format(first_id, last_id, all_fishies)

for shop_id in range(0, total_shops):
    print >> sys.stderr, "Shop: {}, Fish: {}, Roads: {}".format(shop_id, shop_fishies[shop_id], shop_roads[shop_id])

start = time.time()
print SyncShopper().findLeast(all_fishies, shop_fishies, shop_roads, first_id, last_id)
end = time.time()
print >> sys.stderr, "Took time: {}".format(end - start)
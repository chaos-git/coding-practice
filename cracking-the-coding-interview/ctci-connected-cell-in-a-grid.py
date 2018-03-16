def get_biggest_region(grid):
    region_max = 0
    visited = set()
    width = len(grid)
    height = len(grid[0])

    for x in range(width):
        for y in range (height):
            cell = (x, y)
            if cell in visited or not grid[x][y]:
                continue
            region_max = max(region_max, process_region(grid, width, height, visited, cell))            
    return region_max

def process_region(grid, width, height, visited, cell):
    queue = [cell]
    size = 0
    while queue:
        current = queue.pop()
        if current in visited or not grid[current[0]][current[1]]:
            continue

        visited.add(current)
        size += 1
        for x in range(max(0, current[0] - 1), min(width, current[0] + 2)):
            for y in range(max(0, current[1] - 1), min(height, current[1] + 2)):
                queue.append((x,y))
    return size

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)

print get_biggest_region(grid)

s = int(raw_input().strip())

seen = { 0: 1 }
def calc_climbs(steps_remaining):
    if steps_remaining in seen:
        return seen[steps_remaining]
    
    ways = sum([
        calc_climbs(steps_remaining - steps)
        for steps in range(1, min(3, steps_remaining) + 1)
    ])
    
    seen[steps_remaining] = ways
    return ways

for a0 in xrange(s):
    n = int(raw_input().strip())
    print calc_climbs(n)


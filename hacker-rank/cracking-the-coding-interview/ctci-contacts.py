seen = {}

def add(name):
    for i in range(len(name)):
        prefix = name[:i+1]
        seen[prefix] = seen.get(prefix, 0) + 1

def find(prefix):
    print seen.get(prefix, 0)

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    (add if op == 'add' else find)(contact)

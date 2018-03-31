import sys

for line in list(sys.stdin)[1:]:
    (a, b, x) = tuple(map(int, line.split()))
    print int(((a ** b) / float(x)) + 0.5) * x # the extra half causes int() to round to nearest
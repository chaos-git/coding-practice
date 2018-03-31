import sys

n = int(raw_input())

if n % 2:
    print "Weird"

if not n % 2 and n in range(2,6):
    print "Not Weird"

if not n % 2 and n in range(6,21):
    print "Weird"

if not n % 2 and n > 20:
    print "Not Weird"

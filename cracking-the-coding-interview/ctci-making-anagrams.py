def number_needed(a, b):
    seen = {}
    for letter in a:
        seen[letter] = seen.get(letter, 0) + 1
    for letter in b:
        seen[letter] = seen.get(letter, 0) - 1

    return sum(map(abs, seen.values()))

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

import sys

class Parser:
    def parse(self, input):
        string_count = int(input[0])
        strings = [string.strip() for string in input[1:string_count + 1]]
        queries = [query.strip() for query in input[2 + string_count:]]
        return (strings, queries)

(strings, queries) = Parser().parse(list(sys.stdin))

str_dict = {}
for string in strings:
    str_dict[string] = str_dict.get(string, 0) + 1

for query in queries:
    print str_dict.get(query, 0)
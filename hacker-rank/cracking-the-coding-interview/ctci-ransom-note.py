def ransom_note(magazine, ransom):
    required_words = {}
    for word in ransom:
        required_words[word] = required_words.get(word, 0) + 1
    
    unfound_count = len(ransom)
    for word in magazine:
        if not required_words.get(word, 0):
            continue

        required_words[word] -= 1
        unfound_count -= 1
        if unfound_count == 0:
            return True

    return False

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')

print "Yes" if ransom_note(magazine, ransom) else "No"

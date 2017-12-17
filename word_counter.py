def word_counter(document):
    words = document.split(' ')
    repeats = {}
    for word in words:
        if word not in repeats:
            repeats[word] = 0
        repeats[word] += 1
    repeats_ascending = sorted(repeats, key = repeats.__getitem__)
    words_used = [(x,repeats[x]) for x in repeats_ascending]
    return words_used
essay = 'test me out yo'

c = word_counter(essay)
print(c)

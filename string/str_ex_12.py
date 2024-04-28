string = input("Napisz zdanie: ")
string = string.split(" ")

words_counter = {}
dictionary_keys = words_counter.keys()

for word in string:
    if word not in dictionary_keys:
        words_counter[word] = 1
    else:
        words_counter[word] += 1

print(words_counter)

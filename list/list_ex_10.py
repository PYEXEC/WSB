example_list = ["fox", "brown", "quick", "hobby", "the"]
word_length = 4
word_n_length_list = []

for word in example_list:
    if len(word) > word_length:
        word_n_length_list.append(word)


print(word_n_length_list)

string = input("Napisz listę wyrazów: ")
words_list = string.split(",")

unique_words_list = []
for word in words_list:
    if word not in unique_words_list:
        unique_words_list.append(word)

words_list = sorted(unique_words_list)
print(words_list)

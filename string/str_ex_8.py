list_of_words = input("Podaj listę wyrazów: ")


def get_the_longest_word(words_list: str):
    the_longest_word = None
    words_list = words_list.split(",")
    for word in words_list:
        if the_longest_word is None:
            the_longest_word = word
        else:
            if len(word) > len(the_longest_word):
                the_longest_word = word

    return the_longest_word, len(the_longest_word)


result = get_the_longest_word(list_of_words)
print(f"The longest word: {result[0]}\n"
      f"Length of the longest word: {result[1]}")

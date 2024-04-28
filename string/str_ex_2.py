word = input("Napisz wyraz: ")


def count_letters_in_string(string: str):
    letters_counter = {}
    dictionary_keys = letters_counter.keys()

    for letter in string:
        if letter not in dictionary_keys:
            letters_counter[letter] = 1
        else:
            letters_counter[letter] += 1

    return letters_counter


result = count_letters_in_string(word)
print(result)

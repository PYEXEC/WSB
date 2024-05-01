# Ex. 1
string = input("Napisz wyraz: ")
print(len(string))

# Ex. 2
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

# Ex. 3
string = input("Napisz wyraz: ")

if len(string) >= 2:
    transformed_string = f"{string[:2]}{string[-2:]}"
else:
    transformed_string = ""

print(transformed_string)

# Ex. 4
word = input("Napisz wyraz: ")

first_letter = word[0].lower()
word = list(word)

for i, letter in enumerate(word):
    if i == 0:
        continue
    else:
        if letter == first_letter:
            word[i] = "$"

word = "".join(word)
print(word)

# Ex. 5
string_1 = input("Napisz pierwszy wyraz: ")
string_2 = input("Napisz drugi wyraz: ")

combined_string = f"{string_2[:2]}{string_1[2:]} {string_1[:2]}{string_2[2:]}"
print(combined_string)

# Ex. 6
string = input("Napisz wyraz: ")

if len(string) >= 3:
    if string[-3:] == "ing":
        string += "ly"
    else:
        string += "ing"

print(string)

# Ex. 7
word = input("Napisz zdanie: ")

if "not" in word and "poor" in word:
    substring_not_index = word.find("not")
    substring_poor_index = word.find("poor")
    poor_substring_length = len("poor")
    if substring_not_index < substring_poor_index:
        word_prior_poor_substring = word[:substring_not_index]
        word_after_poor_substring = word[substring_poor_index + poor_substring_length:]
        word_prior_poor_substring += "good"

        word = f"{word_prior_poor_substring}{word_after_poor_substring}"

print(word)

# Ex. 8
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

# Ex. 9
string = input("Napisz wyraz: ")
index = int(input("Podaj indeks litery do usunięcia: "))

if string != "":
    string = list(string)
    del string[index]
    string = "".join(string)

print(string)

# Ex. 10
string = input("Napisz wyraz: ")

replaced_string = ""
if len(string) >= 2:
    replaced_string = f"{string[-1:]}{string[1:-1]}{string[:1]}"

print(replaced_string)

# Ex. 11
string = input("Napisz wyraz: ")

transformed_string = ""
for i, letter in enumerate(string):
    if i % 2 == 0:
        transformed_string += letter

print(transformed_string)

# Ex. 12
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

# Ex. 13
string = input("Napisz wyraz: ")

print(f"String uppercase: {string.upper()}\n"
      f"String lowercase: {string.lower()}")

# Ex. 14
string = input("Napisz listę wyrazów: ")
words_list = string.split(",")

unique_words_list = []
for word in words_list:
    if word not in unique_words_list:
        unique_words_list.append(word)

words_list = sorted(unique_words_list)
print(words_list)

# Ex. 15
string = input("Napisz wyraz: ")
tag_html = input("Napisz tag HTML: ")


def add_tags(tag: str, sentence: str):
    string_html_formatted = f"<{tag}>{sentence}</{tag}>"

    return string_html_formatted


print(add_tags(tag_html, string))

# Ex. 16
string = input("Napisz zdanie: ")
middle_string = input("Napisz wyraz do wstawienia pośrodku: ")


def insert_string_middle(sentence: str, string_to_insert: str):
    transformed_string = f"{string[:2]}{middle_string}{string[-2:]}"

    return transformed_string


print(insert_string_middle(string, middle_string))

# Ex. 17
string = input("Napisz wyraz: ")


def insert_end(word: str):
    if len(word) >= 2:
        last_two_chars = word[-2:]

        return last_two_chars * 4
    else:
        return "Za krótki wyraz. Minimalna długość: 2"


print(insert_end(string))

# Ex. 18
string = input("Podaj wyraz: ")


def first_three(word: str):
    if len(word) >= 3:
        word = word[:3]

    return word


print(first_three(string))

# Ex. 19
string = input("Napisz wyraz: ")
separator = input("Napisz separator: ")

last_part = string.rsplit(separator)[-1]

print(last_part)

# Ex. 20
string = input("Napisz wyraz: ")

if len(string) % 4 == 0:
    string = "".join(reversed(string))

print(string)

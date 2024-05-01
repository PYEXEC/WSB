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

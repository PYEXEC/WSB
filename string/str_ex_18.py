string = input("Podaj wyraz: ")


def first_three(word: str):
    if len(word) >= 3:
        word = word[:3]

    return word


print(first_three(string))

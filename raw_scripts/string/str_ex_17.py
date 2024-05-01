string = input("Napisz wyraz: ")


def insert_end(word: str):
    if len(word) >= 2:
        last_two_chars = word[-2:]

        return last_two_chars * 4
    else:
        return "Za krótki wyraz. Minimalna długość: 2"


print(insert_end(string))

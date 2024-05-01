string = input("Napisz zdanie: ")
middle_string = input("Napisz wyraz do wstawienia pośrodku: ")


def insert_string_middle(sentence: str, string_to_insert: str):
    transformed_string = f"{string[:2]}{middle_string}{string[-2:]}"

    return transformed_string


print(insert_string_middle(string, middle_string))

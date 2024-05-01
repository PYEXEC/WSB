example_dict_1 = {}
example_dict_2 = {"x": 5}


def check_is_dict_empty(dictionary: dict):
    if dictionary == {}:
        print(f"Słownik {dictionary} jest pusty")
    else:
        print(f"Słownik {dictionary} nie jest pusty")


print(check_is_dict_empty(example_dict_1))
print(check_is_dict_empty(example_dict_2))

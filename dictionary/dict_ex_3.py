example_dict_1 = {1: 10, 2: 20}
example_dict_2 = {3: 30, 4: 40}
example_dict_3 = {5: 50, 6: 60}

dictionary_4 = {}

for d in (example_dict_1, example_dict_2, example_dict_3):
    dictionary_4.update(d)

print(dictionary_4)

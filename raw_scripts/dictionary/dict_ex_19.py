example_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

print(f"Oryginalna lista: {example_list}")

unique_value = set(value for dictionary in example_list for value in dictionary.values())

print(f"Unikalne wartości: {unique_value}")

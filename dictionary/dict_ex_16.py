example_dict = {"x": 5, "y": 2, "z": 1, "a": 5, "b": 7}

result_dict = {}
for key, value in example_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value

print(f"Oryginalny słownik: {example_dict}\n"
      f"Słownik po usunięciu duplikatów: {result_dict}")

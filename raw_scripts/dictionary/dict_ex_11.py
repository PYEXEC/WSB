example_dict = {"x": 3, "y": 10, "z": 1}
key = input("Podaj klucz do usunięcia: ")

print(f"Oryginalny słownik: {example_dict}")
if key in example_dict.keys():
    del example_dict[key]
    print("Klucz usunięty\n"
          f"Słownik po zmianach: {example_dict}")
else:
    print("Nie ma takiego klucza w słowniku")

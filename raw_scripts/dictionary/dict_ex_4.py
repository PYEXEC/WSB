example_dict = {1: 10, 2: 20, 3: 30}

key = int(input("Podaj klucz do sprawdzenia: "))

if key in example_dict.keys():
    print(f"Klucz {key} znajduje się w słowniku")
else:
    print(f"Klucz {key} nie znajduje się w słowniku")

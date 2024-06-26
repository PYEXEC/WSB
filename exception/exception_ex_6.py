def test_index(data, index_list):
    try:
        result = data[index_list]
        print(f"Wartość elementu z indeksu {index_list} wynosi: {result}")
    except IndexError:
        print("Error: Podany indeks wychodzi poza listę")


example_list = [1, 2, 3, 4, 5, 6, 7, 8]
index = int(input("Podaj indeks: "))
test_index(example_list, index)

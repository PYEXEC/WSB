def test_list_operation(test_list: list):
    try:
        list_length = len(test_list)
        print(f"Długość listy wynosi: {list_length}")
    except AttributeError:
        print("Error: Lista nie ma takiego atrybutu jak długość")


example_list = [1, 2, 3, 4, 5]
test_list_operation(example_list)

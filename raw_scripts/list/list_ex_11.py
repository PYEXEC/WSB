example_list_1 = [4, 3, 5, 7, 2, 1, 9]
example_list_2 = [3, 6, 1, 89, 9, 8, 9]


def common_data(list_1: list, list_2: list):
    for x in list_1:
        for y in list_2:
            if x == y:
                return True

    return False


print(common_data(example_list_1, example_list_2))

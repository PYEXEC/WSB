example_list = [4, 13, 6, 43, 7, 31, 9]


def clone_list(original_list: list):
    cloned_list = original_list.copy()

    return cloned_list


print(clone_list(example_list))

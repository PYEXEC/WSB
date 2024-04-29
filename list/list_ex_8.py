empty_list = []
example_list = [4, 3, 1, 56, 4, 3, 1, 7]


def is_empty_list(list_to_check: list):
    if not list_to_check:
        return True
    else:
        return False


print(f"Is {empty_list} empty? {is_empty_list(empty_list)}")
print(f"Is {example_list} empty? {is_empty_list(example_list)}")

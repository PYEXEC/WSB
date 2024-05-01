example_list_1 = [1, 2, 3, 5, 7, 9]
example_list_2 = [1, 2, 6, 8, 9]

difference_list_1_list_2 = list(set(example_list_1) - set(example_list_2))
difference_list_2_list_1 = list(set(example_list_2) - set(example_list_1))

total_difference = difference_list_1_list_2 + difference_list_2_list_1

print(total_difference)

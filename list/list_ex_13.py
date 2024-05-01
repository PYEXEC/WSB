import itertools

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
merged_list = list(itertools.chain(*original_list))

print(merged_list)


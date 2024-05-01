example_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

transformed_list = [x for (i, x) in enumerate(example_list) if i not in (0, 4, 5)]
print(transformed_list)

example_list = [4, 3, 1, 45, 3, 5, 7, 3, 11, 2, 4]
duplicated_numbers = []
unique_list = []

for number in example_list:
    if number not in duplicated_numbers:
        duplicated_numbers.append(number)
        unique_list.append(number)
    else:
        continue

print(unique_list)

example_list = [5, 3, 67, 34, 1, 2, 34, 6, 7]

list_without_even_numbers = []
for number in example_list:
    if number % 2 != 0:
        list_without_even_numbers.append(number)

print(list_without_even_numbers)

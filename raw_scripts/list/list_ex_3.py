example_list = [4, 33, 1, 6, 14, 44, 3, 21, 8]

the_largest_number = None
for number in example_list:
    if the_largest_number is None:
        the_largest_number = number
    else:
        if number > the_largest_number:
            the_largest_number = number

print(the_largest_number)

example_list = [4, 33, 1, 6, 14, 44, 3, 21, 8]

the_smallest_number = None
for number in example_list:
    if the_smallest_number is None:
        the_smallest_number = number
    else:
        if number < the_smallest_number:
            the_smallest_number = number

print(the_smallest_number)

def get_the_highest_value(a: int, b: int, c: int):
    list_of_numbers = [a, b, c]
    the_highest_value = None
    for number in list_of_numbers:
        if the_highest_value is None:
            the_highest_value = number
        else:
            if number > the_highest_value:
                the_highest_value = number

    return the_highest_value


print(get_the_highest_value(10, 12, 11))

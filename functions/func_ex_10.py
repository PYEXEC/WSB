def get_even_numbers(numbers: list):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_even_numbers(example_list))

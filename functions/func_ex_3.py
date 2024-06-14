def multiply_numbers(numbers: tuple):
    total = 1
    for number in numbers:
        total *= number

    return total


print(multiply_numbers((8, 2, 3, -1, 7)))

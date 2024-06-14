def sum_numbers(numbers: tuple):
    total = 0
    for number in numbers:
        total += number

    return total


print(sum_numbers((6, 1, 5, 7, 2, -9)))

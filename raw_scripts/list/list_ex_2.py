example_list = [5, 4, 3, 1, 6]

result = 0
for number in example_list:
    if result == 0:
        result = number
    else:
        result *= number


print(result)

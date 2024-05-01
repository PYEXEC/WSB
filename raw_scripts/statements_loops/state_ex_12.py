numbers_divisible_by_5 = []

numbers = [x for x in input("Podaj liczby: ").split(",")]

for number in numbers:
    x = int(number, 2)

    if x % 5 == 0:
        numbers_divisible_by_5.append(number)

print(",".join(numbers_divisible_by_5))

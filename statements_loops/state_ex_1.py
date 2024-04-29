numbers = []

for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        numbers.append(str(number))

print(", ".join(numbers))

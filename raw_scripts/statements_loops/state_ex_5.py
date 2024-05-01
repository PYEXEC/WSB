example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_counter = 0
odd_counter = 0
for number in example_list:
    if number % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(f"Liczby nieparzyste: {odd_counter}\n"
      f"Liczby parzyste: {even_counter}")

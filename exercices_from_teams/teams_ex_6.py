numbers_list = []
even_counter = 0

for i in range(10):
    number = int(input("Podaj liczbę: "))
    numbers_list.append(number)

    if number % 2 == 0:
        even_counter += 1

print(f"Wprowadzone liczby: {numbers_list}\n"
      f"Liczba liczb parzystych: {even_counter}")

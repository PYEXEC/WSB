even_number = 0

for i in range(10):
    number = int(input("Podaj liczbę: "))

    if number % 2 == 0:
        even_number += 1

print(f"Liczba liczb parzystych: {even_number}")

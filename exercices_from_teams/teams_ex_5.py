i = 0
numbers_counter = 0

while i < 100:
    number = int(input("Podaj liczbę: "))

    i += number
    numbers_counter += 1

print(f"Podano: {numbers_counter} przed osiągnięciem 100")

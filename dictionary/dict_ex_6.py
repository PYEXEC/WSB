number = int(input("Podaj liczbę: "))


dictionary = {}
for n in range(1, number + 1):
    dictionary[n] = n ** 2

print(dictionary)

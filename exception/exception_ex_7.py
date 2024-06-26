try:
    number = int(input("Podaj liczbę: "))
    print(f"Wprowadziłeś: {number}")
except KeyboardInterrupt:
    print("Wprowadzanie danych anulowane przez użytkownika")

def is_number_prime(number: int):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % 2 == 0:
                return False

        return True


test_number = int(input("Podaj liczbę do sprawdzenia: "))
if is_number_prime(test_number):
    print(f"Liczba {test_number} jest liczbą pierwszą")
else:
    print(f"Liczba {test_number} nie jest liczbą pierwszą")

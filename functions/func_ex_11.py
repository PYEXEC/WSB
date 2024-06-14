def is_number_perfect(number: int):
    sum_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i

    return sum_factors == number


test_number = int(input("Podaj liczbę do sprawdzenia: "))
if test_number > 0:
    if is_number_perfect(test_number):
        print(f"Liczba {test_number} jest liczbą doskonałą")
    else:
        print(f"Liczba {test_number} nie jest liczbą doskonałą")
else:
    print("Liczba musi być większa niż 0")

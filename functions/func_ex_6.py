def is_in_range(number: int):
    if number in range(1, 7):
        print(f"Liczba {number} znajduje się w przedziale")
    else:
        print(f"Liczba {number} nie znajduje się w przedziale")


is_in_range(5)
is_in_range(10)

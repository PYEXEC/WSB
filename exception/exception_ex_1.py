a = 5
b = 0


def divide_numbers(x: int, y: int):
    try:
        result = x / y
        print(f"Wynik dzielenia {x} / {y} = {result}")
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")


divide_numbers(a, b)

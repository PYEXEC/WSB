def division(x, y):
    try:
        result = x / y
        print(f"Wynik: {result}")
    except ArithmeticError:
        print("Error: Błąd arytmetyczny")


a = float(input("Podaj dzielną: "))
b = float(input("Podaj dzielnik: "))
division(a, b)

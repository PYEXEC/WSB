def get_factorial(number: int):
    if number == 0:
        return 1
    else:
        return number * get_factorial(number - 1)


n = int(input("Wprowadź liczbę: "))
print(get_factorial(n))

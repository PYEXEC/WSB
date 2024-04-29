def sum_numbers(x, y):
    result = x + y

    if result in range(15, 20):
        return 20
    else:
        return result


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print(sum_numbers(a, b))

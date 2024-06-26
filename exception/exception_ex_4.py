def get_numeric_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Nieprawidłowa wartość. Proszę wpisać prawidłową liczbę zmiennoprzecinkową")


number_1 = get_numeric_input("Wprowadź pierwszą liczbę: ")
number_2 = get_numeric_input("Wprowadź drugą liczbę: ")

result = number_1 * number_2
print(f"Wynik mnożenia liczb {number_1} i {number_2} wynosi {result}")

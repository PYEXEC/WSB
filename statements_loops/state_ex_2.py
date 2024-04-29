temperature = input("Podaj temperaturę: ")

degree = int(temperature[:-1])
unit = None
result = None
if "C" in temperature:
    result = int(round((9 * degree) / 5 + 32))
    unit = "Fahrenheit"
elif "F" in temperature:
    result = int(round((degree - 32) * 5 / 9))
    unit = "Celcius"
else:
    print("Podaj prawidłową jednostkę temperatury")

print(f"Temperatura w {temperature} wynosi w {unit} {result}")

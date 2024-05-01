# Ex. 1
numbers = []

for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        numbers.append(str(number))

print(", ".join(numbers))

# Ex. 2
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

# Ex. 3
from random import randint

generated_number = randint(1, 10)
while True:
    number = int(input("Podaj liczbę od 1 do 9: "))
    if number == generated_number:
        print("Odgadnąłeś liczbę, gratulacje")
        break

# Ex. 4
word = input("Napisz słowo: ")

print(f"Słowo odwrócone: {''.join(reversed(word))}")

# Ex. 5
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_counter = 0
odd_counter = 0
for number in example_list:
    if number % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(f"Liczby nieparzyste: {odd_counter}\n"
      f"Liczby parzyste: {even_counter}")

# Ex. 6
example_list = ["145", 6, (1, 5), [5, 7], {2: 4}, 4.5]

for item in example_list:
    print(f"{item} jest typu {type(item)}")

# Ex. 7
for number in range(0, 7):
    if number % 3 == 0 and number != 0:
        continue

    print(number, end=" ")

# Ex. 8
x = 0
y = 1

while y < 50:
    print(y)
    x, y = y, x + y

# Ex. 9
for number in range(51):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

# Ex. 10
rows_number = int(input("Podaj liczbę wierszy: "))
cols_number = int(input("Podaj liczbę kolumn: "))

two_dimensional_list = [[0 for col in range(cols_number)] for row in range(rows_number)]

for row in range(rows_number):
    for col in range(cols_number):
        two_dimensional_list[row][col] = row * col

print(two_dimensional_list)

# Ex. 11
lines = []

while True:
    user_lines = input("Napisz tekst: ")

    if user_lines:
        lines.append(user_lines.upper())
    else:
        break

for line in lines:
    print(line)

# Ex. 12
numbers_divisible_by_5 = []

numbers = [x for x in input("Podaj liczby: ").split(",")]

for number in numbers:
    x = int(number, 2)

    if x % 5 == 0:
        numbers_divisible_by_5.append(number)

print(",".join(numbers_divisible_by_5))

# Ex. 13
string = input("Napisz ciąg znaków: ")

letters_counter = 0
digits_counter = 0
for char in string:
    if char.isdigit():
        digits_counter += 1
    elif char.isalpha():
        letters_counter += 1

print(f"Letters: {letters_counter}\n"
      f"Digits: {digits_counter}")

# Ex. 14
import re

password = input("Podaj hasło: ")

if not len(password) in range(6, 17):
    print("Hasło nieprawidłowe")
elif not re.search("[a-z]", password):
    print("Hasło nieprawidłowe")
elif not re.search("[0-9]", password):
    print("Hasło nieprawidłowe")
elif not re.search("[A-Z]", password):
    print("Hasło nieprawidłowe")
elif not re.search("[$#@]", password):
    print("Hasło nieprawidłowe")
else:
    print("Hasło prawidłowe")

# Ex. 15
every_digit_even_in_number_list = []

for i in range(100, 401):
    number = str(i)
    if int(number[0]) % 2 == 0 and int(number[1]) % 2 == 0 and int(number[2]) % 2 == 0:
        every_digit_even_in_number_list.append(number)

print(",".join(every_digit_even_in_number_list))

# Ex. 16
dog_age = int(input("Podaj wiek psa: "))

if dog_age < 0:
    print("Wiek musi być liczbą większą od 0")
    exit()
elif dog_age <= 2:
    dog_age_in_human = dog_age * 10.5
else:
    dog_age_in_human = 21 + (dog_age - 2) * 4

print(f"Wiek psa w latach ludzkich wynosi: {dog_age_in_human}")

# Ex. 17
letter = input("Podaj literę: ")

if letter in ("a", "e", "i", "o", "u"):
    print(f"{letter} jest samogłoską")
elif letter == "y":
    print(f"Czasami litera {letter} w alfabecie angielskim jest samogłoską, a czasami spółgłoską")
else:
    print(f"{letter} jest spółgłoską")

# Ex. 18
import calendar

months_list = "Lista miesięcy: "
for month in calendar.month_name:
    months_list += f"{month} "

print(months_list)
month_name = input("Wprowadź nazwę miesiąca spośród podanych: ")

if month_name == "February":
    print("Liczba dni: 28/29")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("Liczba dni: 31")
elif month_name in ("April", "June", "September", "November"):
    print("Liczba dni: 30")
else:
    print("Nieprawidłowa nazwa miesiąca")

# Ex. 19
def sum_numbers(x, y):
    result = x + y

    if result in range(15, 20):
        return 20
    else:
        return result


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print(sum_numbers(a, b))

# Ex. 20
try:
    string = int(input("Napisz ciąg znaków: "))
    print("Podany ciąg znaków jest liczbą całkowitą")
except ValueError:
    print("Podany ciąg znaków nie jest liczbą całkowitą")

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

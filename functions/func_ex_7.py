def count_upper_and_lower_chars(string: str):
    upper_chars_counter = 0
    lower_char_counter = 0
    for char in string:
        if char.isupper():
            upper_chars_counter += 1
        elif char.islower():
            lower_char_counter += 1

    return upper_chars_counter, lower_char_counter


counters = count_upper_and_lower_chars("The quick Brow Fox")
print(f"Liczba znaków z małej litery: {counters[1]}\n"
      f"Liczba znaków z dużej litery: {counters[0]}")

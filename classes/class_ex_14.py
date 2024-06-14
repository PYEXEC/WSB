class Converter:
    def __init__(self):
        self.roman_to_decimal_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def roman_to_decimal(self, roman_number):
        number = 0
        for i in range(len(roman_number)):
            if i > 0 and self.roman_to_decimal_dict[roman_number[i]] > self.roman_to_decimal_dict[roman_number[i - 1]]:
                number += self.roman_to_decimal_dict[roman_number[i]] - 2 * self.roman_to_decimal_dict[roman_number[i - 1]]
            else:
                number += self.roman_to_decimal_dict[roman_number[i]]

        return number


converter = Converter()
print(converter.roman_to_decimal("MVI"))
print(converter.roman_to_decimal("IX"))
print(converter.roman_to_decimal("C"))

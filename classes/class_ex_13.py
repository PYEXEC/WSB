class Converter:
    def __init__(self):
        self.decimal_to_roman_dict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

    def decimal_to_roman(self, number):
        decimal_numbers = list(reversed(self.decimal_to_roman_dict.keys()))
        roman_numbers = list(reversed(self.decimal_to_roman_dict.values()))
        roman_number = ""
        i = 0
        while number > 0:
            for _ in range(number // decimal_numbers[i]):
                roman_number += roman_numbers[i]
                number -= decimal_numbers[i]
            i += 1

        return roman_number


converter = Converter()
print(converter.decimal_to_roman(1))
print(converter.decimal_to_roman(1936))

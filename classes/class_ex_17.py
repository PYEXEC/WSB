class Example:
    @staticmethod
    def sum_two_numbers(numbers: list, target: int):
        lookup = {}
        for i, num in enumerate(numbers):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i


numbers_list = [10, 20, 10, 40, 50, 15, 25]
target_number = 50
indexes = Example().sum_two_numbers(numbers_list, target_number)
print(f"Indeksy liczb, których suma równa się {target_number} to:\n"
      f"Indeks pierwszej liczby: {indexes[0]}\n"
      f"Indeks drugiej liczby: {indexes[1]}")

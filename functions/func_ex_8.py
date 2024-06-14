def get_distinct_values(numbers: list):
    numbers = set(numbers)

    return numbers


sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
distinct_values = list(get_distinct_values(sample_list))
print(f"{sample_list}\n"
      f"{distinct_values}")

square_numbers = []

for i in range(1, 31):
    square_numbers.append(i ** 2)


print(f"{square_numbers[:5]}\n"
      f"{square_numbers[-5:]}")

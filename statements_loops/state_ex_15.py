every_digit_even_in_number_list = []

for i in range(100, 401):
    number = str(i)
    if int(number[0]) % 2 == 0 and int(number[1]) % 2 == 0 and int(number[2]) % 2 == 0:
        every_digit_even_in_number_list.append(number)

print(",".join(every_digit_even_in_number_list))

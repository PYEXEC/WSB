from random import randint

n = int(input("Proszę podać długość listy: "))

numbers_list = []
for i in range(n):
    number = randint(1, 50)
    numbers_list.append(number)

for index, number in enumerate(numbers_list):
    if number in range(11, 21):
        del numbers_list[index]


print(numbers_list)

string = input("Napisz wyraz: ")

transformed_string = ""
for i, letter in enumerate(string):
    if i % 2 == 0:
        transformed_string += letter

print(transformed_string)

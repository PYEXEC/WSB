string = input("Napisz wyraz: ")

if len(string) >= 2:
    transformed_string = f"{string[:2]}{string[-2:]}"
else:
    transformed_string = ""

print(transformed_string)

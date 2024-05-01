string = input("Napisz wyraz: ")

replaced_string = ""
if len(string) >= 2:
    replaced_string = f"{string[-1:]}{string[1:-1]}{string[:1]}"

print(replaced_string)

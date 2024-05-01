string = input("Napisz wyraz: ")
separator = input("Napisz separator: ")

last_part = string.rsplit(separator)[-1]

print(last_part)

string = input("Napisz wyraz: ")

if len(string) % 4 == 0:
    string = "".join(reversed(string))

print(string)

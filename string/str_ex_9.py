string = input("Napisz wyraz: ")
index = int(input("Podaj indeks litery do usunięcia: "))

if string != "":
    string = list(string)
    del string[index]
    string = "".join(string)

print(string)

try:
    string = int(input("Napisz ciąg znaków: "))
    print("Podany ciąg znaków jest liczbą całkowitą")
except ValueError:
    print("Podany ciąg znaków nie jest liczbą całkowitą")

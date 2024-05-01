letter = input("Podaj literę: ")

if letter in ("a", "e", "i", "o", "u"):
    print(f"{letter} jest samogłoską")
elif letter == "y":
    print(f"Czasami litera {letter} w alfabecie angielskim jest samogłoską, a czasami spółgłoską")
else:
    print(f"{letter} jest spółgłoską")

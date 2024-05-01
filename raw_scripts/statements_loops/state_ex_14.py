import re

password = input("Podaj hasło: ")

if not len(password) in range(6, 17):
    print("Hasło nieprawidłowe")
elif not re.search("[a-z]", password):
    print("Hasło nieprawidłowe")
elif not re.search("[0-9]", password):
    print("Hasło nieprawidłowe")
elif not re.search("[A-Z]", password):
    print("Hasło nieprawidłowe")
elif not re.search("[$#@]", password):
    print("Hasło nieprawidłowe")
else:
    print("Hasło prawidłowe")

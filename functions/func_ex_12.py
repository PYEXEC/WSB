def is_string_palindrome(word: str):
    if word == word[::-1]:
        return True
    else:
        return False


string = input("Napisz wyraz: ")
if is_string_palindrome(string):
    print("Podany wyraz jest palindromem")
else:
    print("Podany wyraz nie jest palindromem")

string_1 = input("Napisz pierwszy wyraz: ")
string_2 = input("Napisz drugi wyraz: ")

combined_string = f"{string_2[:2]}{string_1[2:]} {string_1[:2]}{string_2[2:]}"
print(combined_string)

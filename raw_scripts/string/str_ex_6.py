string = input("Napisz wyraz: ")

if len(string) >= 3:
    if string[-3:] == "ing":
        string += "ly"
    else:
        string += "ing"

print(string)

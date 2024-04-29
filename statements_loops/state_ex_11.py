lines = []

while True:
    user_lines = input("Napisz tekst: ")

    if user_lines:
        lines.append(user_lines.upper())
    else:
        break

for line in lines:
    print(line)

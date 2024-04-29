rows_number = int(input("Podaj liczbę wierszy: "))
cols_number = int(input("Podaj liczbę kolumn: "))

two_dimensional_list = [[0 for col in range(cols_number)] for row in range(rows_number)]

for row in range(rows_number):
    for col in range(cols_number):
        two_dimensional_list[row][col] = row * col

print(two_dimensional_list)

def pascal_triangle(number: int):
    trow = [1]
    y = [0]

    for i in range(max(number, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]

    return number >= 1


pascal_triangle(6)

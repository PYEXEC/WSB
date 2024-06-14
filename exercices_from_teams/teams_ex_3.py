from random import randint


def roll_dice():
    return randint(1, 6)


result = roll_dice()
print(f"Wynik rzutu kostką: {result}")

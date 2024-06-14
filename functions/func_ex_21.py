import math
from time import sleep


def delay(function, ms, *args):
    sleep(ms / 1000)

    return function(*args)


print("Pierwiastek kwadratowy po określonym opóźnieniu w milisekundach: ")
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))

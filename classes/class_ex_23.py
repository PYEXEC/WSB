from math import pi


class Circle:
    def __init__(self, radius: (int, float)):
        self.radius = radius
        self.PI = pi

    def calculate_area(self):
        return round(pi * self.radius ** 2, 2)

    def calculate_perimeter(self):
        return round(2 * pi * self.radius, 2)


circle_object = Circle(5)
print(f"Pole koła: {circle_object.calculate_area()}")
print(f"Obwód koła: {circle_object.calculate_perimeter()}")

class Rectangle:
    def __init__(self, length: (int, float), width: (int, float)):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle_object = Rectangle(12, 5)
print(rectangle_object.calculate_area())

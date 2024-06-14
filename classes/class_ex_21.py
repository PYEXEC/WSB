class Example:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Podaj ciąg znaków: ")

    def print_string(self):
        print(self.string.upper())


instance = Example()
instance.get_string()
instance.print_string()

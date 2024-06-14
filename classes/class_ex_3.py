class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


person = Person("Jan", "Kowalski", 36)
print(person.__dict__)

class ExampleDict(object):
    def __init__(self):
        self.x = "John"
        self.y = "Derreck"
        self.z = "Carl"


example_dict_instance = ExampleDict()
print(example_dict_instance.__dict__)

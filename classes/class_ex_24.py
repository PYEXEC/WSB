class TestClass:
    pass


class Example:
    @staticmethod
    def get_class_name(instance):
        return type(instance).__name__


test_instance = TestClass()
print(Example().get_class_name(test_instance))

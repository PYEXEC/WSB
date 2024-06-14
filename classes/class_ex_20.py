class Example:
    @staticmethod
    def reverse_sentence(sentence: str):
        return " ".join(reversed(sentence.split()))


instance = Example()
print(instance.reverse_sentence("Przykładowe zdanie"))

# Ex. 1
import operator

example_dict = {1: 3, 5: 5, 8: 1, 4: 9, 3: 2}

sorted_ascending = dict(sorted(example_dict.items(), key=operator.itemgetter(1)))
sorted_descending = dict(sorted(example_dict.items(), key=operator.itemgetter(1), reverse=True))

print(f"Oryginalny słownik: {example_dict}\n"
      f"W kolejności rosnącej: {sorted_ascending}\n"
      f"W kolejności malejącej: {sorted_descending}")

# Ex. 2
example_dict = {0: 10, 1: 20}

print(f"Oryginalny słownik: {example_dict}")

example_dict[2] = 50

print(f"Słownik po dodaniu wartości: {example_dict}")

# Ex. 3
example_dict_1 = {1: 10, 2: 20}
example_dict_2 = {3: 30, 4: 40}
example_dict_3 = {5: 50, 6: 60}

dictionary_4 = {}

for d in (example_dict_1, example_dict_2, example_dict_3):
    dictionary_4.update(d)

print(dictionary_4)

# Ex. 4
example_dict = {1: 10, 2: 20, 3: 30}

key = int(input("Podaj klucz do sprawdzenia: "))

if key in example_dict.keys():
    print(f"Klucz {key} znajduje się w słowniku")
else:
    print(f"Klucz {key} nie znajduje się w słowniku")

# Ex. 5
example_dict = {"x": 10, "y": 20, "z": 30}

for key, value in example_dict.items():
    print(f"{key} -> {value}")

# Ex. 6
number = int(input("Podaj liczbę: "))


dictionary = {}
for n in range(1, number + 1):
    dictionary[n] = n ** 2

print(dictionary)

# Ex. 7
dictionary = {}

for number in range(1, 16):
    dictionary[number] = number ** 2

print(dictionary)

# Ex. 8
example_dict_1 = {"a": 100, "b": 200}
example_dict_2 = {"c": 300, "d": 400}

merged_dictionary = example_dict_1.copy()
merged_dictionary.update(example_dict_2)

print(merged_dictionary)

# Ex. 9
example_dict = {"x": 100, "y": 5, "z": -9}

result = sum(example_dict.values())
print(result)

# Ex. 10
example_dict = {"x": 5, "y": 7, "z": 2}

result = 1
for value in example_dict.values():
    result *= value

print(result)

# Ex. 11
example_dict = {"x": 3, "y": 10, "z": 1}
key = input("Podaj klucz do usunięcia: ")

print(f"Oryginalny słownik: {example_dict}")
if key in example_dict.keys():
    del example_dict[key]
    print("Klucz usunięty\n"
          f"Słownik po zmianach: {example_dict}")
else:
    print("Nie ma takiego klucza w słowniku")

# Ex. 12
example_keys = ["one", "two", "three", "four"]
example_values = [1, 2, 3, 4]

example_dict = dict(zip(example_keys, example_values))
print(example_dict)

# Ex. 13
example_dict = {"c": 5, "l": 2, "z": 7, "a": 15, "b": 3}

for key in sorted(example_dict.keys()):
    print(f"{key}: {example_dict[key]}")

# Ex. 14
example_dict = {"a": 6, "b": 1, "c": 9, "d": 3, "e": 2}

minimum = min(example_dict.values())
maximum = max(example_dict.values())

print(f"Najmniejsza wartość: {minimum}\n"
      f"Największa wartość: {maximum}")

# Ex. 15
class ExampleDict(object):
    def __init__(self):
        self.x = "John"
        self.y = "Derreck"
        self.z = "Carl"


example_dict_instance = ExampleDict()
print(example_dict_instance.__dict__)

# Ex. 16
example_dict = {"x": 5, "y": 2, "z": 1, "a": 5, "b": 7}

result_dict = {}
for key, value in example_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value

print(f"Oryginalny słownik: {example_dict}\n"
      f"Słownik po usunięciu duplikatów: {result_dict}")

# Ex. 17
example_dict_1 = {}
example_dict_2 = {"x": 5}


def check_is_dict_empty(dictionary: dict):
    if dictionary == {}:
        print(f"Słownik {dictionary} jest pusty")
    else:
        print(f"Słownik {dictionary} nie jest pusty")


print(check_is_dict_empty(example_dict_1))
print(check_is_dict_empty(example_dict_2))

# Ex. 18
from collections import Counter

example_dict_1 = {"a": 100, "b": 200, "c": 300}
example_dict_2 = {"a": 300, "b": 200, "d": 400}

result_dict = Counter(example_dict_1) + Counter(example_dict_2)
print(result_dict)

# Ex. 19
example_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

print(f"Oryginalna lista: {example_list}")

unique_value = set(value for dictionary in example_list for value in dictionary.values())

print(f"Unikalne wartości: {unique_value}")

# Ex. 20
import itertools

example_dict = {"1": ["a", "b"], "2": ["c", "d"]}

for pair in itertools.product(*[example_dict[k] for k in sorted(example_dict.keys())]):
    print("".join(pair))

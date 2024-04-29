from collections import Counter

example_dict_1 = {"a": 100, "b": 200, "c": 300}
example_dict_2 = {"a": 300, "b": 200, "d": 400}

result_dict = Counter(example_dict_1) + Counter(example_dict_2)
print(result_dict)

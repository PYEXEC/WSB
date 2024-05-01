import itertools

example_dict = {"1": ["a", "b"], "2": ["c", "d"]}

for pair in itertools.product(*[example_dict[k] for k in sorted(example_dict.keys())]):
    print("".join(pair))

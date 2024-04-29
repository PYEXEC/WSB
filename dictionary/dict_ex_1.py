import operator

example_dict = {1: 3, 5: 5, 8: 1, 4: 9, 3: 2}

sorted_ascending = dict(sorted(example_dict.items(), key=operator.itemgetter(1)))
sorted_descending = dict(sorted(example_dict.items(), key=operator.itemgetter(1), reverse=True))

print(f"Oryginalny słownik: {example_dict}\n"
      f"W kolejności rosnącej: {sorted_ascending}\n"
      f"W kolejności malejącej: {sorted_descending}")

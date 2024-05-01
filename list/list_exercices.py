# Ex. 1
example_list = [5, 3, 2, 1, 16, 4]

print(sum(example_list))

# Ex. 2
example_list = [5, 4, 3, 1, 6]

result = 0
for number in example_list:
    if result == 0:
        result = number
    else:
        result *= number


print(result)

# Ex. 3
example_list = [4, 33, 1, 6, 14, 44, 3, 21, 8]

the_largest_number = None
for number in example_list:
    if the_largest_number is None:
        the_largest_number = number
    else:
        if number > the_largest_number:
            the_largest_number = number

print(the_largest_number)

# Ex. 4
example_list = [4, 33, 1, 6, 14, 44, 3, 21, 8]

the_smallest_number = None
for number in example_list:
    if the_smallest_number is None:
        the_smallest_number = number
    else:
        if number < the_smallest_number:
            the_smallest_number = number

print(the_smallest_number)

# Ex. 5
example_letters_list = ["f", "o", "o", "b", "a", "r"]

string = "".join(example_letters_list)
print(string)

# Ex. 6
example_list = [5, 3, 1, 7, 8, 10]

print(example_list.index(7))

# Ex. 7
example_list = [4, 3, 1, 45, 3, 5, 7, 3, 11, 2, 4]
duplicated_numbers = []
unique_list = []

for number in example_list:
    if number not in duplicated_numbers:
        duplicated_numbers.append(number)
        unique_list.append(number)
    else:
        continue

print(unique_list)

# Ex. 8
empty_list = []
example_list = [4, 3, 1, 56, 4, 3, 1, 7]


def is_empty_list(list_to_check: list):
    if not list_to_check:
        return True
    else:
        return False


print(f"Is {empty_list} empty? {is_empty_list(empty_list)}")
print(f"Is {example_list} empty? {is_empty_list(example_list)}")

# Ex. 9
example_list = [4, 13, 6, 43, 7, 31, 9]


def clone_list(original_list: list):
    cloned_list = original_list.copy()

    return cloned_list


print(clone_list(example_list))

# Ex. 10
example_list = ["fox", "brown", "quick", "hobby", "the"]
word_length = 4
word_n_length_list = []

for word in example_list:
    if len(word) > word_length:
        word_n_length_list.append(word)


print(word_n_length_list)

# Ex. 11
example_list_1 = [4, 3, 5, 7, 2, 1, 9]
example_list_2 = [3, 6, 1, 89, 9, 8, 9]


def common_data(list_1: list, list_2: list):
    for x in list_1:
        for y in list_2:
            if x == y:
                return True

    return False


print(common_data(example_list_1, example_list_2))

# Ex. 12
example_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

transformed_list = [x for (i, x) in enumerate(example_list) if i not in (0, 4, 5)]
print(transformed_list)

# Ex. 13
import itertools

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
merged_list = list(itertools.chain(*original_list))

print(merged_list)

# Ex. 14
example_list = [5, 3, 67, 34, 1, 2, 34, 6, 7]

list_without_even_numbers = []
for number in example_list:
    if number % 2 != 0:
        list_without_even_numbers.append(number)

print(list_without_even_numbers)

# Ex. 15
from random import sample

example_list = ["Red", "Blue", "Yellow", "Green", "Black", "Brown"]

print(sample(example_list, 6))

# Ex. 16
square_numbers = []

for i in range(1, 31):
    square_numbers.append(i ** 2)


print(f"{square_numbers[:5]}\n"
      f"{square_numbers[-5:]}")

# Ex. 17
import random

example_list = ["Red", "Green", "Blue", "Brown", "Black", "White", "Pink"]

print(random.choice(example_list))

# Ex. 18
from itertools import permutations

example_list = [1, 2, 3, 4, 5]

print(list(permutations(example_list)))

# Ex. 19
example_list_1 = [1, 2, 3, 5, 7, 9]
example_list_2 = [1, 2, 6, 8, 9]

difference_list_1_list_2 = list(set(example_list_1) - set(example_list_2))
difference_list_2_list_1 = list(set(example_list_2) - set(example_list_1))

total_difference = difference_list_1_list_2 + difference_list_2_list_1

print(total_difference)

# Ex. 20
example_list = [35, 1, 54, 6, 1, 78, 7]

for index, value in enumerate(example_list):
    print(f"Indeks {index} wartość {value}")

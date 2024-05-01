word = input("Napisz zdanie: ")

if "not" in word and "poor" in word:
    substring_not_index = word.find("not")
    substring_poor_index = word.find("poor")
    poor_substring_length = len("poor")
    if substring_not_index < substring_poor_index:
        word_prior_poor_substring = word[:substring_not_index]
        word_after_poor_substring = word[substring_poor_index + poor_substring_length:]
        word_prior_poor_substring += "good"

        word = f"{word_prior_poor_substring}{word_after_poor_substring}"

print(word)

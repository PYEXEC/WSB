import string


def is_string_pangram(sentence: str, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str_set = set(sentence.lower())
    return alphaset <= str_set


print(is_string_pangram('The quick brown fox jumps over the lazy dog'))

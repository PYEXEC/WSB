string = input("Napisz wyraz: ")
tag_html = input("Napisz tag HTML: ")


def add_tags(tag: str, sentence: str):
    string_html_formatted = f"<{tag}>{sentence}</{tag}>"

    return string_html_formatted


print(add_tags(tag_html, string))

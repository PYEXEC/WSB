def make_bold(string):
    def wrapped():
        return f"<b>{string()}</b>"

    return wrapped


def make_italic(string):
    def wrapped():
        return f"<i>{string()}</i>"

    return wrapped


def make_underline(string):
    def wrapped():
        return f"<u>{string()}</u>"

    return wrapped


@make_bold
@make_italic
@make_underline
def hello():
    return "Hello World!"


print(hello())

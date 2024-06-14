def sort_items(items: str):
    items_list = items.split("-")
    items_list.sort()
    items_string = "-".join(items_list)

    return items_string


string = input("Podaj listę słów oddzielonych myślnikiem: ")
print(sort_items(string))

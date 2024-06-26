def open_file(path: str):
    encoding = input("Wprowadź kodowanie (ASCII, UTF-16, UTF-8) dla pliku: ")
    try:
        with open(path, "r", encoding=encoding) as f:
            file_content = f.read()

        print(f"Zawartość pliku: {file_content}")
    except UnicodeDecodeError:
        print("Error: Problem z kodowaniem podczas odczytywania pliku")


file_path = input("Wprowadź ścieżkę do pliku: ")
open_file(file_path)

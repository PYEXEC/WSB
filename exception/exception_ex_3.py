def open_file(path: str):
    try:
        with open(path, "r") as f:
            file_content = f.read()

        print(f"Zawartość pliku: {file_content}")
    except FileNotFoundError:
        print("Error: Plik nie istnieje")


file_path = input("Wprowadź ścieżkę do pliku: ")
open_file(file_path)

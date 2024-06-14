class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
        else:
            print("Przedmiot nie znajduje się w magazynie")

    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Nazwa produktu: {item['item_name']}, Ilość produktu na stanie: {item['stock_count']}, Cena: {item['price']}"
        else:
            return "Przedmiot nie znajduje się w magazynie"


inventory = Inventory()

inventory.add_item("I478", "Żelazko", 58, 137.99)
inventory.add_item("I983", "Ekspres do kawy", 0, 250)
inventory.add_item("I135", "Suszarka", 5, 59.78)

print("Informacje o produktach:")
print(inventory.check_item_details("I478"))
print(inventory.check_item_details("I983"))
print(inventory.check_item_details("I135"))

print("Zmiana ceny produktu o identyfikatorze: I135")
inventory.update_item("I135", 10, 49.99)
inventory.check_item_details("I135")

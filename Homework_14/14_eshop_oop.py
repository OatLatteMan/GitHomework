class Item():
    def __init__(self, name: str, label: str, count: int, price: int):
        self.name = name
        self.label = label
        self.count = count
        self.price = price

item_1 = Item('Panska Mikina', 'Puma', 10, 890)
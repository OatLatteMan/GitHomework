# kosik_16.py

import datetime as dt

class An_Item:

    counter = 0

    def __init__(self, name: str, price: float, volume: float, _type: str, eat_to: dt.datetime = None):
        self.__class__.counter += 1

        self.id = self.counter
        self.name = name
        self.price = price
        self.eat_to = eat_to
        self.volume = volume
        self._type = _type

    def __str__(self):
        of_type = '' # if an item is food, than measurement is in KG's, if drink - it is Liters
        due_dt = f'Until {self.eat_to}' if self.eat_to else ''

        if self._type == 'solid':
            of_type = ' kg'
        elif self._type == 'liquid':
            of_type = ' L'

        return f"It's {self.name}. Costs {self.price} Kč. {self.volume}{of_type}. {due_dt}"

    def change_price(self, new_price):
        self.price = new_price


class Shopping_Cart:
    def __init__(self, name: str):
        self.name = name
        self.items = {}

    def add_item(self, item: An_Item):
        if item.id not in self.items:
            self.items[item.id] = item

    def remove_item(self, item: An_Item):
        return self.remove_item_by_id(item.id)

    def remove_item_by_id(self, item_id: int):
        try:
            removed_item = self.items.pop(item_id)
            return removed_item
        except KeyError:
            return None

    def count_total_price(self):
        total_price = 0

        for items in self.items.values():
            total_price += items.price

        return f"The total price of items in actual shopping cart is {round(total_price, 2)} Kč"

    def show(self):
        for items in self.items.values():
            print(items)


item1 = An_Item('Mayo', 19.9, 0.25, 'liquid', dt.datetime(2025, 1, 31))
item2 = An_Item('Cheese nuts', 49.9, 0.5, 'solid')
item3 = An_Item('Staropramen Beer', 29.9, 0.5, 'liquid')
item4 = An_Item('Pizza', 40.9, 0.33, 'solid', dt.datetime(2025, 1, 23))

shop_cart1 = Shopping_Cart('For thursday')

shop_cart1.add_item(item1)
shop_cart1.add_item(item2)
shop_cart1.add_item(item3)
shop_cart1.add_item(item4)



shop_cart1.show()
# print('--------------------------------')

# shop_cart1.remove_item(item4)
# shop_cart1.remove_item_by_id(3)

# shop_cart1.show()

""""""
# kosik_16_app.py

# from kosik_16 import An_Item, Shopping_Cart
# import kosik_16
from kosik_16 import *

shop_cart = Shopping_Cart("For Thursday's")

while True:
    command = input('Put a command: ')

    if command == 'add':
        name = input('Add an item name: ')
        price = float(input("Put an item's price: "))
        volume = float(input("Put an item's volume: "))
        _type = str(input("Put an item's type: "))
        shop_cart.add_item(An_Item(name, price, volume, _type))

    if command == 'remove':
        remove_an_item = int(input('An item to remove: '))
        shop_cart.remove_item_by_id(remove_an_item)

    shop_cart.show()


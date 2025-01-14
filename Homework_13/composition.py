class Girlfriend:
    def __init__(self, name, loyalty, age, green_flags):
        self.name = name
        self.loyalty = loyalty
        self.age = age
        self.green_flags = green_flags

one_of = Girlfriend('Zuzka', False, 25, ['roses', 'lana', 'cranberries'])
print(one_of.green_flags)

################################################################
################################################################

class Liquid:
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am liquid')

class E_Liquid(Liquid):
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f"I am the {self.name} liquid for vape and an electronic cigarette")

lychee = E_Liquid('lychee-ice')
lychee.who_am_i()

################################################################

class Laptop:
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am a laptop')

class Gaming_laptop(Laptop):
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f"I am the {self.name} gaming laptop for gaming and programming purposes")

asus_rog = Gaming_laptop('Asus ROG')
asus_rog.who_am_i()

################################################################

class Taxi:
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am a taxi')

class Business_taxi(Taxi):
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f"I am the {self.name} business taxi for pure comfortable and luxury rides")

mercedes = Business_taxi('mercedes')
mercedes.who_am_i()
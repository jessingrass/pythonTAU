# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))

Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()


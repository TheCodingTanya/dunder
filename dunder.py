class Product:
    def __init__(self, name, price):
        self.name = name  # property
        self.price = price # property

    # str較為簡短
    def __str__(self):
      # return self.name + ' $ ' + str(self.price)
        return f'{self.name} ${self.price}'
    
    # representation
    def __repr__(self):
        return f'<Product({self.name}, {self.price})>'

    def __add__(self, other):
        if isinstance(other, str):
            self.name += other
        if isinstance(other, Product):
            return [self, other]

    def __mul__(self, other):
        re = []
        if isinstance(other, int):
            for _ in range(other):
                re.append(self)
        return re

p1 = Product('珍珠奶茶', 60) # instance
p2 = Product('義大利麵', 220)
# p + '白玉'
print(p1 * 5)
# print(p)
# print(repr(p))

class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __getitem__(self, key):
        return self.products[key]

s = ShoppingCart([p1, p2])
print(s[0])
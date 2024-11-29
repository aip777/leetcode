
class Product():
    def __init__(self, name:str=None, price:int=0, products_name:str=None, message:str=None):
        self.name = name
        self.price = price
        self.message = message
        self.products_name = []

    def __add__(self, other):
        total = self.price + other.price
        return Product(message="Total Price", price=total)

    def __str__(self):
        return f'{self.message}, {str(self.price)}'

obj1 = Product("Pen", 200)
obj2 = Product("Books", 500)
result = obj1 + obj2
print(result)

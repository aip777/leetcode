
class Book(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __call__(self,name):
        print("This call method")
        return f'{name}, {self.price}'
obj = Book("Crazy Spoken",550)
print(obj('Crazy Spoken 2'))


"""
Клас AddToCartCommand представляє команду додавання товару до кошика, яка приймає об'єкт кошика і додаваний товар.
Метод execute викликає метод add_product об'єкта кошика.
Клас User представляє об'єкт, що ініціює виконання команди. У цьому прикладі метод add_to_cart створює новий об'єкт
команди, додає його до списку команд користувача та виконує команду.
Клас ShoppingCart представляє об'єкт, який виконує команду - додає товар до кошика.
У цьому прикладі користувач створює команду додавання товару до кошика та виконує її. Додавання товару до кошика
відбувається через метод add_to_cart, який додає команду до списку команд користувача.
"""


# Клас, що представляє команду
class AddToCartCommand:
    def __init__(self, cart, product):
        self.cart = cart
        self.product = product

    def execute(self):
        self.cart.add_product(self.product)


# Клас, що представляє об'єкт, що ініціює виконання команди
class User:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def add_to_cart(self, cart, product):
        command = AddToCartCommand(cart, product)
        self.commands.append(command)
        command.execute()


# Клас кошика, в який додаються товари
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


# Створення об'єктів
user = User('John')
cart = ShoppingCart()
product1 = {'name': 'Laptop', 'price': 1000}
product2 = {'name': 'Mouse', 'price': 50}

# Виконання команди
user.add_to_cart(cart, product1)
user.add_to_cart(cart, product2)

# Виведення списку товарів у кошику
print([p['name'] for p in cart.products])

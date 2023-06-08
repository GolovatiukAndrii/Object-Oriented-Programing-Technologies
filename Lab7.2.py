# Абстрактний клас товару
class Product:
    def accept(self, visitor):
        pass


# Конкретний клас товару - Товар
class Item(Product):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def accept(self, visitor):
        visitor.visit(self)


# Конкретний клас відвідувача - Перевірка наявності товарів
class StockChecker:
    def visit(self, item):
        if item.quantity > 0:
            print(f"{item.name} є в наявності")
        else:
            print(f"{item.name} відсутній на складі")


# Клас кошика з товарами
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def accept(self, visitor):
        for item in self.items:
            item.accept(visitor)


# Створення об'єктів товарів
item1 = Item("Телефон", 5)
item2 = Item("Ноутбук", 0)
item3 = Item("Планшет", 3)

# Створення кошика
shopping_cart = ShoppingCart()
shopping_cart.add_item(item1)
shopping_cart.add_item(item2)
shopping_cart.add_item(item3)

# Створення об'єкта відвідувача
stock_checker = StockChecker()

# Перевірка наявності товарів у кошику
shopping_cart.accept(stock_checker)

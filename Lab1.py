"""
Технічне завдання:
Реалізувати інтернет-магазин для продажу різних типів товарів. Для ццього слід розробити програмне забезпечення
з можливістю динамічного ибору категорій продуктів, які можуть бути вибрані до корзини користувачем.

Вимоги:
1. Розробити ПЗ на моввві програмування Python
2. Реалізувати створення продуктів (паттерн "фабричний метод")
3. У системі реалізувати можливвість додавання нових категорій в майбтньому (паттерн "абстрактна фабрика")
4. Система має відслідковувати кількість доданих товарів у кошик та їх ціну.
5. Розробити графічний інтерфейс користувача з можливістю додавання товарів у корзину та перегляду корзини
"""

from abc import ABC, abstractmethod  # Імпортуємо необхідні модулі


# Створюємо абстрактний клас, який визначає метод створення продукту
class ProductFactory(ABC):

    @abstractmethod
    def create_product(self, **kwargs):
        pass


# Створюємо конкретну фабрику, яка буде створювати книжки
class BookFactory(ProductFactory):

    def create_product(self, **kwargs):
        return Book(**kwargs)


# Створюємо конкретну фабрику, яка буде створювати футболки
class ShirtFactory(ProductFactory):

    def create_product(self, **kwargs):
        return Shirt(**kwargs)


# Створюємо базовий клас для продуктів
class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price


# Створюємо конкретний клас для книжок, який наслідується від базового класу "Product"
class Book(Product):

    def __init__(self, name, price, author, genre):
        super().__init__(name, price)
        self.author = author
        self.genre = genre


# Створюємо конкретний клас для футболок, який наслідується від базового класу "Product"
class Shirt(Product):

    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color


# Створюємо функцію, яка створює продукт з використанням переданої фабрики та аргументів
def create_product(factory, **kwargs):
    return factory.create_product(**kwargs)


# Створюємо об'єкти книжок та футболок з використанням відповідних фабрик та деяких аргументів
book = create_product(BookFactory(), name="The Great Gatsby", price=10.99, author="F. Scott Fitzgerald",
                      genre="Classic")
shirt = create_product(ShirtFactory(), name="Nike T-Shirt", price=19.99, size="M", color="Blue")

# Виводимо деяку інформацію про кожен продукт
print(f"Book: {book.name} by {book.author} ({book.genre}) - ${book.price}")
print(f"Shirt: {shirt.size} size, {shirt.color} color - ${shirt.price}")

"""
Технічне завдання:
Реалізувати інтернет-магазин для продажу різних типів товарів.
1. Створити базу даних продуктів та зберігати в ній інформацію про назву, ціну та опис продуктів.
2. Реалізувати можливість перегляду списку продуктів на головній сторінці магазину.
3. Реалізувати можливість додавання продуктів до кошика та оформлення замовлення.
4. Реалізувати можливість редагування замовлення (видалення, зміна кількості тощо) та оформлення оплати та доставки.
5. Забезпечити можливість перегляду історії замовлень та статусу їх виконання.
"""

import copy


# Патерн прототипу
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def clone(self):
        return copy.deepcopy(self)


class ProductRegistry:
    def __init__(self):
        self.products = {}

    def add_product(self, name, product):
        self.products[name] = product

    def get_product(self, name):
        return self.products[name].clone()


# Патерн будівельника
class Order:
    def __init__(self):
        self.products = []
        self.shipping_address = None
        self.billing_address = None
        self.payment_method = None

    def add_product(self, product):
        self.products.append(product)

    def set_shipping_address(self, address):
        self.shipping_address = address

    def set_billing_address(self, address):
        self.billing_address = address

    def set_payment_method(self, method):
        self.payment_method = method

    def place_order(self):
        for number, item in enumerate(self.products):
            print(f"Товар №{number+1}: {item.name}. Ціна: {item.price}")
        print(f"Адреса доставки: {self.shipping_address}\n"
              f"Метод оплати:{self.payment_method}")
        pass


class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_product(self, product):
        self.order.add_product(product)

    def set_shipping_address(self, address):
        self.order.set_shipping_address(address)

    def set_billing_address(self, address):
        self.order.set_billing_address(address)

    def set_payment_method(self, method):
        self.order.set_payment_method(method)

    def get_order(self):
        return self.order


if __name__ == '__main__':
    product1 = Product("Телефон", 1000, "Мобільний телефон з екраном 6 дюймів")
    product2 = Product("Ноутбук", 1500, "Легкий та потужний ноутбук з процесором Intel")
    product_registry = ProductRegistry()
    product_registry.add_product("телефон", product1)
    product_registry.add_product("ноутбук", product2)

    order_builder = OrderBuilder()
    product_copy1 = product_registry.get_product("телефон")
    product_copy2 = product_registry.get_product("ноутбук")
    order_builder.add_product(product_copy1)
    order_builder.add_product(product_copy2)
    order_builder.set_shipping_address("вул. Шевченка, 1, м. Київ, Україна")
    order_builder.set_billing_address("вул. Шевченка, 1, м. Київ, Україна")
    order_builder.set_payment_method("Кредитна картка")
    order = order_builder.get_order()
    order.place_order()

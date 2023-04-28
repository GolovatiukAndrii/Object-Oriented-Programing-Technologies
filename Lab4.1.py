from abc import ABC, abstractmethod


# Абстрактний клас для команди
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Конкретна реалізація команди для додавання товару до кошика
class AddToCartCommand(Command):
    def __init__(self, product_id):
        self.product_id = product_id

    def execute(self):
        # Логіка додавання товару до кошика за допомогою product_id
        print(f"Added product with ID {self.product_id} to cart")


# Конкретна реалізація команди для заповнення адресних даних
class FillAddressCommand(Command):
    def __init__(self, address):
        self.address = address

    def execute(self):
        # Логіка заповнення адресних даних за допомогою address
        print(f"Filled address information: {self.address}")


# Конкретна реалізація команди для вибору способу доставки
class ChooseDeliveryCommand(Command):
    def __init__(self, delivery_method):
        self.delivery_method = delivery_method

    def execute(self):
        # Логіка вибору способу доставки за допомогою delivery_method
        print(f"Chose delivery method: {self.delivery_method}")


# Конкретна реалізація команди для вибору способу оплати
class ChoosePaymentCommand(Command):
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def execute(self):
        # Логіка вибору способу оплати за допомогою payment_method
        print(f"Chose payment method: {self.payment_method}")


# Клас для макрокоманди
class OrderCommand:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()


# Створення об'єктів команд
add_to_cart = AddToCartCommand(1)
fill_address = FillAddressCommand("123 Main St")
choose_delivery = ChooseDeliveryCommand("Express")
choose_payment = ChoosePaymentCommand("Credit Card")

# Створення макрокоманди та додавання в неї окремих команд
order = OrderCommand()
order.add_command(add_to_cart)
order.add_command(fill_address)
order.add_command(choose_delivery)
order.add_command(choose_payment)

# Виконання макрокоманди
order.execute()

from abc import ABC, abstractmethod


# Абстрактний клас для типів товарів
class Product(ABC):
    def __init__(self, payment_method):
        self.payment_method = payment_method

    @abstractmethod
    def get_product_details(self):
        pass

    def process_payment(self):
        self.payment_method.process_payment()


# Конкретний клас товару - Електроніка
class Electronics(Product):
    def __init__(self, payment_method):
        super().__init__(payment_method)

    def get_product_details(self):
        return "Електроніка"


# Конкретний клас товару - Одяг
class Clothing(Product):
    def __init__(self, payment_method):
        super().__init__(payment_method)

    def get_product_details(self):
        return "Одяг"


# Абстрактний клас для способів оплати
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        pass


# Конкретний клас способу оплати - Кредитна карта
class CreditCardPayment(PaymentMethod):
    def process_payment(self):
        print("Оплата кредитною карткою")


# Конкретний клас способу оплати - PayPal
class PayPalPayment(PaymentMethod):
    def process_payment(self):
        print("Оплата через PayPal")


# Використання патерну "Міст"
# Створення об'єктів товарів з відповідними способами оплати
electronics = Electronics(CreditCardPayment())
clothing = Clothing(PayPalPayment())

# Використання об'єктів товарів
print(electronics.get_product_details())
electronics.process_payment()

print(clothing.get_product_details())
clothing.process_payment()

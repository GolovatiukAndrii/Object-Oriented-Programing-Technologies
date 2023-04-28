from abc import ABC, abstractmethod


# Абстрактний клас для шаблонного методу оплати замовлення
class OrderPaymentTemplate(ABC):
    def process_payment(self, order):
        self.verify_funds(order)
        self.charge_customer(order)
        self.update_order_status(order)

    @abstractmethod
    def verify_funds(self, order):
        pass

    @abstractmethod
    def charge_customer(self, order):
        pass

    def update_order_status(self, order):
        print(f"Order {order.id} has been paid")


# Конкретна реалізація шаблонного методу оплати замовлення з використанням кредитної картки
class CreditCardPayment(OrderPaymentTemplate):
    def verify_funds(self, order):
        # Логіка перевірки наявності коштів на рахунку клієнта
        print("Funds have been verified")

    def charge_customer(self, order):
        # Логіка зняття коштів з рахунку клієнта
        print("Payment has been processed with credit card")


# Конкретна реалізація шаблонного методу оплати замовлення з використанням PayPal
class PayPalPayment(OrderPaymentTemplate):
    def verify_funds(self, order):
        # Логіка перевірки наявності коштів на PayPal-рахунку клієнта
        print("Funds have been verified")

    def charge_customer(self, order):
        # Логіка зняття коштів з PayPal-рахунку клієнта
        print("Payment has been processed with PayPal")


# Приклад використання шаблонного методу для оплати замовлення з використанням кредитної картки
class Order:
    def __init__(self, id):
        self.id = id


order = Order(1)
payment_processor = CreditCardPayment()
payment_processor.process_payment(order)

# Приклад використання шаблонного методу для оплати замовлення з використанням PayPal
order = Order(2)
payment_processor = PayPalPayment()
payment_processor.process_payment(order)

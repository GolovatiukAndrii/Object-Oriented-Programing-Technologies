from abc import ABC, abstractmethod


# Абстрактний клас для платіжного шлюзу
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Конкретний платіжний шлюз - PayPal
class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        # Логіка обробки платежу за допомогою PayPal
        print(f"Payment processed via PayPal: {amount}$")


# Конкретний платіжний шлюз - Stripe
class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        # Логіка обробки платежу за допомогою Stripe
        print(f"Payment processed via Stripe: {amount}$")


# Посередник, що взаємодіє зі сторонніми платіжними шлюзами
class PaymentMediator:
    def __init__(self):
        self.payment_gateways = []

    def add_payment_gateway(self, payment_gateway):
        self.payment_gateways.append(payment_gateway)

    def process_payment(self, amount):
        for gateway in self.payment_gateways:
            gateway.process_payment(amount)


# Створення об'єктів платіжних шлюзів
paypal_gateway = PayPalGateway()
stripe_gateway = StripeGateway()

# Створення посередника
payment_mediator = PaymentMediator()
payment_mediator.add_payment_gateway(paypal_gateway)
payment_mediator.add_payment_gateway(stripe_gateway)

# Обробка платежу через посередника
payment_mediator.process_payment(100)

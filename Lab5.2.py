from abc import ABC, abstractmethod


# Абстрактний клас для стану замовлення
class OrderState(ABC):
    @abstractmethod
    def process_order(self, order):
        pass


# Конкретний клас для стану "новий"
class NewOrderState(OrderState):
    def process_order(self, order):
        order.state = ExecutedOrderState()
        print(f"Order #{order.id} has been executed")


# Конкретний клас для стану "виконаний"
class ExecutedOrderState(OrderState):
    def process_order(self, order):
        raise Exception(f"Order #{order.id} has already been executed")


# Клас замовлення
class Order:
    def __init__(self, id):
        self.id = id
        self.state = NewOrderState()

    def process(self):
        self.state.process_order(self)


# Приклад використання
order1 = Order(1)
order2 = Order(2)

# Виконуємо замовлення зі станом "новий"
order1.process()
# Виконуємо замовлення зі станом "новий"
order2.process()

# Виконуємо замовлення зі станом "виконаний" (повинна виникнути помилка)
order1.process()

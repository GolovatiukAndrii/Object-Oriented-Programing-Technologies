"""
Є абстрактний клас OrderProcessingStrategy, який містить метод process_order(),
який буде реалізований в класах-стратегіях. Класи ExpressDeliveryStrategy та StandardDeliveryStrategy
реалізують цей метод для обробки замовлень з експрес-доставкою та стандартною доставкою відповідно.

Клас Order містить інформацію про товари та тип доставки. Клас OrderProcessor приймає об'єкт-стратегію для обробки
замовлення та містить метод process_order(), який викликає метод process_order() на переданому об'єкті-стратегії.
В останньому рядку коду створюється об'єкт processor, який використовує ExpressDeliveryStrategy для обробки
замовлення з експрес-доставкою.
"""

from abc import ABC, abstractmethod


class OrderProcessingStrategy(ABC):
    @abstractmethod
    def process_order(self, order):
        pass


class ExpressDeliveryStrategy(OrderProcessingStrategy):
    def process_order(self, order):
        print("Processing order with express delivery")


class StandardDeliveryStrategy(OrderProcessingStrategy):
    def process_order(self, order):
        print("Processing order with standard delivery")


class Order:
    def __init__(self, items, delivery_type):
        self.items = items
        self.delivery_type = delivery_type


class OrderProcessor:
    def __init__(self, processing_strategy):
        self.processing_strategy = processing_strategy

    def process_order(self, order):
        self.processing_strategy.process_order(order)


items = ["item1", "item2", "item3"]
order = Order(items, "express")
processor = OrderProcessor(ExpressDeliveryStrategy())
processor.process_order(order)

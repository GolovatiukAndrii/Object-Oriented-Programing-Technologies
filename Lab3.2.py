"""
Є класи Observable та Observer, які реалізують паттерн Спостерігач.
Клас Observable зберігає список спостерігачів та містить методи для додавання, видалення та сповіщення
спостерігачів про зміни. Клас Observer є базовим класом для всіх спостерігачів та містить метод update(),
який буде викликаний при сповіщенні про зміни.
Класи EmailNotifier та SMSNotifier є конкретними реалізаціями класу Observer, які надсилають електронні листи та
повідомлення SMS відповідно. Клас Store містить список товарів та об'єкт Observable, який буде сповіщати спостерігачі
про зміни в цьому списку.
В останніх рядках коду створюється об'єкт store, додаються нові товари та сповіщаються всі зареєстровані спостерігачі
про ці зміни.
"""


class Observable:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, new_items):
        for observer in self._observers:
            observer.update(new_items)


class Observer:
    def update(self, new_items):
        pass


class EmailNotifier(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, new_items):
        print(f"Sending email notification to {self.email} about new items: {new_items}")


class SMSNotifier(Observer):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, new_items):
        print(f"Sending SMS notification to {self.phone_number} about new items: {new_items}")


class Store:
    def __init__(self):
        self.items = []
        self.observable = Observable()

    def add_item(self, item):
        self.items.append(item)
        self.observable.notify_observers(self.items)


store = Store()
email_notifier = EmailNotifier("example@example.com")
sms_notifier = SMSNotifier("+1234567890")
store.observable.register_observer(email_notifier)
store.observable.register_observer(sms_notifier)
store.add_item("New item 1")
store.add_item("New item 2")

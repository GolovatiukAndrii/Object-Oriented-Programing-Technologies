class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_state(self):
        return OrderMemento(self.items)

    def restore_state(self, memento):
        self.items = memento.get_saved_items()

    def __str__(self):
        return f"Order: {', '.join(self.items)}"


class OrderMemento:
    def __init__(self, items):
        self.saved_items = items

    def get_saved_items(self):
        return self.saved_items


class OrderHistory:
    def __init__(self):
        self.mementos = []

    def save_order_state(self, order):
        self.mementos.append(order.get_state())

    def restore_order_state(self, order):
        if self.mementos:
            last_state = self.mementos.pop()
            order.restore_state(last_state)
        else:
            print("No order states available.")

    def __str__(self):
        return f"Order History: {len(self.mementos)} saved states."


# Створення об'єкту замовлення
order = Order()
order.add_item("Item 1")
order.add_item("Item 2")
print(order)

# Створення об'єкту історії замовлень
order_history = OrderHistory()

# Збереження стану замовлення
order_history.save_order_state(order)

# Зміни в замовленні
order.add_item("Item 3")
order.remove_item("Item 1")
print(order)

# Відновлення попереднього стану замовлення
order_history.restore_order_state(order)
print(order)

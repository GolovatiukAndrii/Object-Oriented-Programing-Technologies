class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item}' added to the shopping cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removed from the shopping cart.")
        else:
            print(f"Item '{item}' not found in the shopping cart.")

    def checkout(self):
        total_items = len(self.items)
        print(f"Checkout completed. Total items in the shopping cart: {total_items}.")


class OrderFacade:
    def __init__(self):
        self.shopping_cart = ShoppingCart()

    def add_item_to_cart(self, item):
        self.shopping_cart.add_item(item)

    def remove_item_from_cart(self, item):
        self.shopping_cart.remove_item(item)

    def place_order(self):
        self.shopping_cart.checkout()


# Використання фасаду для взаємодії з інтерфейсною підсистемою
order = OrderFacade()
order.add_item_to_cart("Phone")
order.add_item_to_cart("Headphones")
order.remove_item_from_cart("Headphones")
order.place_order()

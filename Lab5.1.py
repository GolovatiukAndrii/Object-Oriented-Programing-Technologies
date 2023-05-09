class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class ProductIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product

    def has_next(self):
        return self.index < len(self.products)


def find_products(products, category, max_price):
    iterator = ProductIterator(products)
    result = []
    while iterator.has_next():
        product = next(iterator)
        if product.category == category and product.price <= max_price:
            result.append(product)
    return result


products = [
    Product("Product 1", "Category 1", 10),
    Product("Product 2", "Category 2", 20),
    Product("Product 3", "Category 1", 30),
    Product("Product 4", "Category 2", 40),
    Product("Product 5", "Category 1", 50),
]

category = "Category 1"
max_price = 30
result = find_products(products, category, max_price)
print(result)
# Output: [Product(name='Product 1', category='Category 1', price=10), Product(name='Product 3', category='Category 1', price=30)]

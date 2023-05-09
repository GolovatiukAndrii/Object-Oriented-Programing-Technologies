import random


def RandBool():
    random_number = random.randint(0, 1)
    value = bool(random_number)
    return value


class RequestHandler:
    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass


class DatabaseHandler(RequestHandler):
    def handle_request(self, request):
        if request.type == 'database':
            # Логіка пошуку товару в базі даних
            found = RandBool()
            if found:
                print('Товар знайдено в базі даних')
            else:
                self.successor.handle_request(request)


class WarehouseHandler(RequestHandler):
    def handle_request(self, request):
        if request.type == 'warehouse':
            # Логіка пошуку товару на складі
            found = RandBool()
            if found:
                print('Товар знайдено на складі')
            else:
                self.successor.handle_request(request)


class SupplierHandler(RequestHandler):
    def handle_request(self, request):
        if request.type == 'supplier':
            # Логіка звернення до постачальника
            found = RandBool()
            if found:
                print('Товар знайдено в постачальника')
            else:
                print('Товар не знайдено')


class Request:
    def __init__(self, type):
        self.type = type


# Створення обробників запитів
db_handler = DatabaseHandler()
wh_handler = WarehouseHandler()
supplier_handler = SupplierHandler()

# Встановлення ланцюга обов'язків
db_handler.set_successor(wh_handler)
wh_handler.set_successor(supplier_handler)

# Запуск обробки запиту
request = Request('database')
db_handler.handle_request(request)

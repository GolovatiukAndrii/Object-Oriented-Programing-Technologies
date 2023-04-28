# Object-Oriented-Programing-Technologies

### Технічне завдання:
Реалізувати інтернет-магазин для продажу різних типів товарів. Для ццього слід розробити програмне забезпечення
з можливістю динамічного ибору категорій продуктів, які можуть бути вибрані до корзини користувачем.

# Lab1
### Вимоги:
1. Розробити ПЗ на мові програмування Python
2. Реалізувати створення продуктів (паттерн "фабричний метод")
3. У системі реалізувати можливвість додавання нових категорій в майбтньому (паттерн "абстрактна фабрика")
4. Система має відслідковувати кількість доданих товарів у кошик та їх ціну.
5. Розробити графічний інтерфейс користувача з можливістю додавання товарів у корзину та перегляду корзини

# Lab2
### Технічне завдання:
1. Створити базу даних продуктів та зберігати в ній інформацію про назву, ціну та опис продуктів.
2. Реалізувати можливість перегляду списку продуктів на головній сторінці магазину.
3. Реалізувати можливість додавання продуктів до кошика та оформлення замовлення.
4. Реалізувати можливість редагування замовлення (видалення, зміна кількості тощо) та оформлення оплати та доставки.
5. Забезпечити можливість перегляду історії замовлень та статусу їх виконання.

### Вимоги:
1. Реалізувати клас, який буде містити назву, ціну та опис товару (Product).
2. Реалізувати метод для глибинного копіювання продуктів (clone).
3. Розробити клас для зберігання прототипів продуктів та надає методи для додавання нових продуктів (ProductRegistry).
4. Розробити метод для оформлення замовлення (place_order).
5. Реалізувати клас для будування замовлення (OrderBuilder).
6. Реалізувати метод для повернення готового замовлення (get_order).

# Lab3
### Технічне завдання:
1. Створити різні стратегії обробки замовлень залежно від рівня та способо доставки.
2. Розробити можливість сповіщення користувачів про статус замовлення та оновлення інформації про товари.
3. Реалізувати можливість додавання товару до кошика користувача та видалення його звідти.

## File Lab3.1
Створено абстрактний клас OrderProcessingStrategy, що містить метод process_order(), що реалізується в класах-стратегіях.
Класи ExpressDeliveryStrategy та StandardDeliveryStrategy реалізують цей метод для обробки замовлень з експрес-доставкою та стандартною доставкою відповідно.
Клас Order містить інформацію про товари та тип доставки. Клас OrderProcessor приймає об'єкт-стратегію для обробки замовлення та містить метод process_order(), який викликає метод process_order() на переданому об'єкті-стратегії.

## File Lab3.2
Є класи Observable та Observer, які реалізують паттерн Спостерігач. Клас Observable зберігає список спостерігачів та містить методи для додавання, видалення та сповіщення спостерігачів про зміни. Клас Observer є базовим класом для всіх спостерігачів та містить метод update(), який буде викликаний при сповіщенні про зміни.
Класи EmailNotifier та SMSNotifier є конкретними реалізаціями класу Observer, які надсилають електронні листи та SMS повідомлення відповідно. Клас Store містить список товарів та об'єкт Observable, який буде сповіщати спостерігачів про зміни в цьому списку.

## File Lab3.3
Клас AddToCartCommand представляє команду додавання товару до кошика, яка приймає об'єкт кошика і додаваний товар. Метод execute викликає метод add_product об'єкта-кошика. Клас User представляє об'єкт, що ініціює виконання команди. Метод add_to_cart створює новий об'єкт
команди, додає його до списку команд користувача та виконує команду. Клас ShoppingCart представляє об'єкт, який виконує команду - додає товар до кошика.

# Lab4
### Технічне завдання:
1. Створити можливість оформлення замовлення, яка буде включати в себе: 
1.1 додавання товарів до кошика
1.2 заповнення адресних даних
1.3 вибір способу доставки та оплати

2.Створити можливість оплати замовлення, яка буде включати в себе: 
2.1 перевірка наявності коштів на рахунку
2.2 зняття коштів з рахунку
2.3 оновлення статусу замовлення

## File Lab4.1
Паттерн "Макрокоманда"
Були визначені абстрактний клас (OrderCommand) команди та чотири конкретні реалізації команд для додавання товару до кошика, заповнення адресних даних, вибору способу доставки та вибору способу оплати. Кожна з цих команд має метод execute, який містить відповідну логіку для виконання команди. Абстрактний клас має метод add_command, який додає команду до списку та метод execute, який виконує всі команди зі списку одну за одною, викликаючи метод execute для кожної команди.

## File Lab4.2
Шаблонний метод
Створено абстрактний клас OrderPaymentTemplate, який містить послідовність кроків, які потрібно виконати для обробки платежу за замовлення. Ці кроки включають перевірку наявності коштів, зняття коштів та оновлення статусу замовлення.
verify_funds() та charge_customer() - методи, які будуть перевизначені у підкласах.
update_order_status() - метод, який оновлює статус замовлення після успішної оплати.
CreditCardPayment та PayPalPayment - підкласи OrderPaymentTemplate, які реалізують конкретну логіку перевірки наявності коштів та зняття коштів з рахунків клієнтів для оплати замовлення з використанням кредитної картки та PayPal відповідно.

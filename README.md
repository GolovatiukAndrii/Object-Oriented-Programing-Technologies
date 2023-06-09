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


# Lab5
### Технічне завдання:
1. Розробити функції пошуку товарів 
1.1 Функція пошуку товарів з певними характеристиками
1.2 Функція сортування списку товарів за різними критеріями
1.3 Функція фільтрації списку товарів за різними параметрами (наприклад, за ціною або категорією)

2. Реалізувати зміну різних станів замовлення
2.1 Стан "Нове замовлення"
2.2 Стан "Замовлення в обробці"
2.3 Стан "Замовлення відправлено"
2.4 Стан "Замовлення доставлено"

3. Розробити функцію, що обробляє запити користувачів на різних рівнях або етапах операції замовлення
3.1 Перевірка доступності товару в базі даних
3.2 Перевірка доступності товару на складі
3.3 Перевірка доступності товару в постачальника

## File Lab5.1
Для пошуку товарів з певними характеристиками за допомогою патерну Ітератор було створено клас ProductIterator, який імплементує інтерфейс Iterator та має методи __init__, __next__ та has_next. Цей ітератор використовується для ітерування по списку товарів і знаходить лише ті, які задовольняють певні характеристики. Була написана функція find_products_by_category_and_price, яка використовує ітератор для перевірки кожного товару на задовольнення критеріїв категорії та ціни. Кінцевий результат - список товарів, які задовольняють задані характеристики.

## File Lab5.2
Було створено абстрактний клас OrderState, який визначає метод process_order, що виконує замовлення. Конкретні реалізації класу - NewOrderState і ExecutedOrderState - представляють стани "новий" і "виконаний" відповідно.
Клас Order представляє замовлення і містить стан, який можна змінити за допомогою методу process. Якщо стан замовлення "новий", викликається метод process_order для стану "виконаний". Якщо стан замовлення "виконаний", викидається помилка.

## File Lab5.3
Було створено клас RequestHandler, який є базовим для всіх класів-обробників запитів. У ньому оголошується метод handle_request(request), який має за завдання обробляти отримані запити.
Класи DatabaseHandler, WarehouseHandler та SupplierHandler є нащадками класу RequestHandler і реалізують конкретні обробники запитів. У кожному з цих класів перевіряється тип отриманого запиту і, якщо тип відповідає типу, який може бути оброблений, виконується певна логіка. Якщо товар був знайдений, виводиться повідомлення про його наявність. Якщо товар не був знайдений, обробка запиту передається наступному обробнику за ланцюгом.
Клас Request є об'єктом, який містить тип запиту і передається на обробку відповідному обробнику запиту.

# Lab6
### Технічне завдання:
1. Реалізувати розрахунок вартості замовлення залежно від різних факторів, таких як кількість товарів, їх ціни, знижки. (Інтерпритатор)
2. Реалізувати взаємодію зі сторонніми сервісами (платіжні шлюзи та системи доставки) (Медіатор)

## File Lab6.1
Використання патерну Інтерпретатор може спростити процес підрахунку загальної вартості замовлення та зробити його більш гнучким і розширюваним.

Context визначає контекст, в якому відбуваються обчислення. Контекст містить поля discount (знижка) та tax (податок).
Expression є абстрактним класом, який визначає метод interpret(context). Він буде перевизначений у підкласах та виконуватиме інтерпретацію виразів.
TerminalExpression є конкретним підкласом Expression і представляє термінальний вираз.
DiscountExpression та TaxExpression є підкласами Expression та представляють вирази зі знижкою та податком відповідно. Вони отримують вираз та значення знижки або податку в конструкторі, і виконують обчислення відповідно до цих значень.

У головній частині коду:
Створюється об'єкт Context, що представляє контекст обчислень.
Створюються термінальні вирази: base_price представляє базову ціну замовлення (100).
Створюються складні вирази з використанням DiscountExpression та TaxExpression. discounted_price використовується для обчислення ціни зі знижкою (заданою як 0.1) від базової ціни. final_price використовується для обчислення кінцевої ціни з урахуванням податку (заданого як 0.05) від зниженої ціни.
Виконується інтерпретація final_price за допомогою методу interpret(context), де context містить відповідні значення знижки та податку. Отримана кінцева ціна замовлення виводиться на екран.

## File Lab6.2
PaymentGateway є абстрактним класом, що визначає метод process_payment(amount). Цей клас представляє платіжний шлюз, і його підкласи будуть реалізовувати конкретні платіжні шлюзи.
PayPalGateway та StripeGateway є конкретними платіжними шлюзами, що успадковують від PaymentGateway. Кожен з цих класів реалізує свою власну логіку обробки платежу за допомогою відповідного платіжного сервісу.
PaymentMediator є посередником, який взаємодіє зі сторонніми платіжними шлюзами. Він містить список платіжних шлюзів та методи для додавання шлюзів та обробки платежу. У методі process_payment(amount) посередник просто передає запит на обробку платежу кожному платіжному шлюзу зі свого списку.

У головній частині коду:
Створюються об'єкти конкретних платіжних шлюзів PayPalGateway та StripeGateway.
Створюється об'єкт PaymentMediator, який буде виконувати роль посередника для обробки платежів.
Додаються платіжні шлюзи до посередника за допомогою методу add_payment_gateway(payment_gateway).
Викликається метод process_payment(amount) посередника з передачею суми платежу. Посередник передає цей запит кожному з доданих платіжних шлюзів, і кожен шлюз обробляє платіж відповідно до своєї логіки.


# Lab7

### Технічне завдання:
1. Реалізувати збереження стану кошика замовлення в інтернет-магазині ("Зберігач")
2. Реалізувати перевірку наявності товарів: користувач може перевіряти наявність товарів на складі, обходячи об'єкти складу та перевіряючи їх кількість ("Відвідувач")

## File Lab7.1
Клас Order представляє замовлення і має методи для додавання та видалення товарів з замовлення. Він також має метод get_state, який повертає об'єкт OrderMemento, що містить збережений стан замовлення. Метод restore_state приймає об'єкт OrderMemento і відновлює стан замовлення на основі збереженого стану.
Клас OrderMemento представляє місце зберігання стану замовлення. Він має метод get_saved_items, який повертає збережені товари замовлення.
Клас OrderHistory представляє історію збережених станів замовлень. Він має метод save_order_state, який приймає об'єкт Order і зберігає його поточний стан у вигляді об'єкта OrderMemento. Метод restore_order_state відновлює останній збережений стан замовлення. Якщо станів немає, виводиться повідомлення "No order states available".
У головній частині коду створюється об'єкт order, додаються товари до замовлення і виводиться його поточний стан. Далі створюється об'єкт order_history, якому зберігається стан замовлення за допомогою методу save_order_state. Потім в замовленні вносяться зміни (додається новий товар і видаляється один із товарів) і виводиться змінений стан замовлення. Нарешті, викликається метод restore_order_state об'єкту order_history, який відновлює останній збережений стан замовлення, і виводиться замовлення відновленого стану.

## File Lab7.2
В коді визначений абстрактний клас Product, який містить метод accept, що приймає об'єкт відвідувача (visitor) і не реалізований в цьому класі.
Клас Item є конкретною реалізацією товару. Він успадковує від Product і має свої властивості, такі як назва (name) і кількість (quantity). Клас також реалізує метод accept, який передає об'єкт self відвідувачу, що викликає метод visit відповідного типу відвідувача.
Клас StockChecker є конкретним відвідувачем і містить метод visit, який перевіряє наявність товару. Якщо кількість товару більше 0, виводиться повідомлення про його наявність, інакше виводиться повідомлення про його відсутність.
Клас ShoppingCart представляє кошик з товарами і має метод add_item, що додає товари до кошика. Він також має метод accept, який передає об'єкт відвідувача (visitor) кожному товару у кошику.
У головній частині коду створюються об'єкти товарів (item1, item2, item3) і додаються до кошика shopping_cart. Створюється об'єкт відвідувача stock_checker. Потім метод accept викликається на об'єкті shopping_cart, передаючи об'єкт stock_checker в якості відвідувача. Це спричиняє виклик методу visit на кожному об'єкті товару у кошику, де відбувається перевірка наявності товару та виведення відповідного повідомлення.

# Lab8

### Технічне завдання:
1. Упростити інтерфейсну підсистема: Створити спрощений інтерфейс, який використовується клієнтами для взаємодії з різними складовими системи магазину. (Фасад)
2. Розробити ліниве завантаження (Lazy Loading) (зображення товару). (Замісник)
3. Реалізувати відношення між типами товарів і способами оплати в інтернет-магазині (Міст)

## File Lab8.1
В коді визначено клас ShoppingCart, який представляє кошик з покупками. Він має методи add_item для додавання товару до кошика, remove_item для видалення товару з кошика і checkout для завершення оформлення замовлення. Кожен метод виводить відповідне повідомлення про виконану операцію.
Клас OrderFacade виступає як фасад, який надає спрощений інтерфейс для взаємодії з підсистемою, що складається з класу ShoppingCart. Він має методи add_item_to_cart для додавання товару до кошика, remove_item_from_cart для видалення товару з кошика і place_order для оформлення замовлення.
У головній частині коду створюється об'єкт order класу OrderFacade. Виклики методів add_item_to_cart та remove_item_from_cart на об'єкті order виконують відповідні операції з додаванням та видаленням товарів з кошика. Нарешті, метод place_order виконує оформлення замовлення шляхом виклику методу checkout на об'єкті shopping_cart.
В результаті виконання коду виводяться повідомлення про додавання товарів до кошика, видалення товару з кошика та оформлення замовлення.

## File Lab8.2
У коді визначено клас ProductImage, який представляє зображення товару. Він має метод load_image, який завантажує зображення з заданого шляху і метод display_image, який відображає зображення. Зображення завантажується тільки тоді, коли воно перший раз потрібне для відображення.
Клас LazyLoadingProxy виступає як проксі (замісник) для об'єкту ProductImage. Він отримує оригінальний об'єкт як параметр у конструкторі. Клас LazyLoadingProxy має метод display_image, який викликає метод load_image на оригінальному об'єкті, якщо зображення ще не завантажене, а потім викликає метод display_image на оригінальному об'єкті для відображення зображення.
У головній частині коду створюється об'єкт image_proxy класу LazyLoadingProxy, якому передається об'єкт ProductImage з шляхом до зображення "product1.jpg". При виклику методу display_image на об'єкті image_proxy, проксі спочатку завантажує зображення, якщо воно ще не завантажене, а потім відображає його. При повторному виклику методу display_image зображення відображається без повторного завантаження, оскільки воно вже було завантажено.
Таким чином, за допомогою проксі забезпечується лінива (відкладена) загрузка зображення, що дозволяє економити ресурси, завантажуючи зображення лише при необхідності.

## File Lab8.3
У коді визначені абстрактні класи Product і PaymentMethod. Клас Product представляє товар і містить абстрактний метод get_product_details, який повинен бути реалізований у конкретних підкласах товарів. Він також має метод process_payment, який викликає метод process_payment об'єкта PaymentMethod, що передається у конструкторі.
Класи Electronics і Clothing є конкретними підкласами Product. Вони реалізовують абстрактний метод get_product_details, повертаючи відповідні деталі товару.
Класи CreditCardPayment і PayPalPayment є конкретними підкласами PaymentMethod. Вони реалізують абстрактний метод process_payment, який виводить повідомлення про здійснення оплати.
У головній частині коду створюються об'єкти Electronics і Clothing, передаючи їм відповідні об'єкти PaymentMethod (класи CreditCardPayment і PayPalPayment). За допомогою цих об'єктів виводяться деталі товарів та виконується оплата, викликаючи методи get_product_details і process_payment.
Таким чином, патерн "Міст" дозволяє розділити класи товарів та способи оплати, щоб забезпечити більшу гнучкість та розширюваність системи, а також зменшити залежність між ними.

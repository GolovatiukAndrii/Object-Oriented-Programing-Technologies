class Context:
    def __init__(self):
        self.discount = 0
        self.tax = 0


class Expression:
    def interpret(self, context):
        pass


class TerminalExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class DiscountExpression(Expression):
    def __init__(self, expression, discount):
        self.expression = expression
        self.discount = discount

    def interpret(self, context):
        discounted_value = self.expression.interpret(context) - (self.expression.interpret(context) * self.discount)
        return discounted_value


class TaxExpression(Expression):
    def __init__(self, expression, tax):
        self.expression = expression
        self.tax = tax

    def interpret(self, context):
        taxed_value = self.expression.interpret(context) + (self.expression.interpret(context) * self.tax)
        return taxed_value


# Створення контексту
context = Context()

# Створення термінальних виразів
base_price = TerminalExpression(100)
discounted_price = DiscountExpression(base_price, 0.1)
final_price = TaxExpression(discounted_price, 0.05)

# Розрахунок вартості замовлення
total_price = final_price.interpret(context)
print(f"Total price: {total_price}")

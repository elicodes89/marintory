class Product:

    def __init__(self, name, category, cost, selling_price, stock_quantity, id = None):
        self.name = name
        self.category = category
        self.cost = cost
        self.selling_price = selling_price
        self.stock_quantity = stock_quantity
        self.id = id
class Product:

    def __init__(self, name, category, cost, selling_price, id = None):
        self.name = name
        self.category = category
        self.cost = cost
        self.selling_price = selling_price
        self.stock = []
        self.id = id

    def add_product(self, product):
        self.product.append(product)



    # def stock_level(self, product):
    #     if product in self.stock_quantity:
    #         return self.stock_quantity(product)
    #     else:
    #         return 0
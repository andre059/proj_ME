class Product:
    storing_instances = 0
    discount = 0.15

    def __init__(self, product, product_price, quantity_goods):
        self.product = product
        self.product_price = product_price
        self.quantity_goods = quantity_goods
        self.product_discount = None

    def price_product_in_store(self):
        self.product_price = self.product_price * self.quantity_goods
        return self.product_price

    def price_product_discount(self):
        self.product_discount = (self.product_price / self.quantity_goods) * self.discount


pro_1 = Product("Смартфон", 10000, 20)
pro_2 = Product("Смартфон", 20000, 5)

print(pro_1.price_product_in_store())
print(pro_2.price_product_in_store())

Product.discount = 0.8
pro_1.price_product_discount()
print(pro_1.product_discount)
print(pro_2.product_discount)

print(Product.all)

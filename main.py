class Product:
    all = []
    discount = 0.15  # Скидка на товар 0,15 == 15%

    def __init__(self, product, product_price, quantity_goods):
        """
        Поступление данных о таваре в магазине
        :param product: Наименование товара
        :param product_price: Цена товара
        :param quantity_goods: каоличество товара в магазине
        """
        self.product = product
        self.product_price = product_price
        self.quantity_goods = quantity_goods
        self.all.append(self)

    def price_product_in_store(self):
        """
        подсчет общей стоимости оставшегося товара в магазине
        :return: Общая стоимость
        """
        return self.product_price * self.quantity_goods

    def price_product_discount(self):
        """
        Подсчет скидки на одну еденицу товар
        :return: Цена товара с учетом скидки
        """
        self.product_price = self.product_price * self.discount


pro_1 = Product("Смартфон", 10000, 20)
pro_2 = Product("Ноутбук", 20000, 5)

print(pro_1.price_product_in_store())
print(pro_2.price_product_in_store())

Product.discount = 0.8
pro_1.price_product_discount()
print(pro_1.product_price)
print(pro_2.product_price)

print(Product.all)

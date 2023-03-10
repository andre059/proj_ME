from main import Product


def test_price_product_in_store():
    total_balance = Product("Смартфон", 10000, 20)
    assert total_balance.price_product_in_store() == 200000


def test_price_product_discount():
    discount = Product("Смартфон", 10000, 0.8)
    assert discount.price_product_discount() is None

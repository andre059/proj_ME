from main import Product


def test_price_product_in_store():
    assert Product.price_product_in_store(10000, 20) == 2000000
    # assert entering_data.price_product_in_store(-10000, 20) == -2000000
    # assert entering_data.price_product_in_store(-10000, -20) == 2000000
    # assert entering_data.price_product_in_store(-10000, 0) == 0
    # assert entering_data.price_product_in_store(-10000, 'try') is None


def test_price_product_discount():
    assert Product.price_product_discount(10000, 0.8) == 8000.0
    # assert price_product_discount(10000, -0.8) == -8000.0
    # assert price_product_discount(10000, 0) == 0
    # assert price_product_discount(10000, 1) == 10000
    # assert price_product_discount(10000, 'try') is None

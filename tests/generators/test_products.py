from dataseeder.generators.products import generate_products


def test_generate_products_count(user_ids):
    data = generate_products(user_ids, per_user=5)
    assert len(data) == 15


def test_product_price_positive(user_ids):
    product = generate_products(user_ids, per_user=1)[0]
    assert product["price"] > 0

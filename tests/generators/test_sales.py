from dataseeder.generators.sales import generate_sales


def test_generate_sales(user_ids):
    products = [
        {
            "id": "prod-1",
            "price": 10,
            "stock": 5,
            "user_id": user_ids[0],
        },
    ]

    sales = generate_sales(user_ids, products, sales_per_user=1)

    assert len(sales) == 1
    assert sales[0]["total_amount"] > 0

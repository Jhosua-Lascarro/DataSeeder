from random import choice, randint

from dataseeder.utils.time import random_past_datetime


def generate_sales(
    user_ids: list[str], products: list[dict], sales_per_user: int = 10
) -> list[dict]:
    """Generate a list of sales given a list of user_ids and products."""

    sales = []

    products_by_user = {}
    for p in products:
        products_by_user.setdefault(p["user_id"], []).append(p)

    for user_id in user_ids:
        user_products = products_by_user.get(user_id, [])
        if not user_products:
            continue

        for _ in range(sales_per_user):
            product = choice(user_products)

            if product["stock"] <= 0:
                continue

            quantity = randint(1, min(5, product["stock"]))
            created_at = random_past_datetime()

            sales.append(
                {
                    "user_id": user_id,
                    "product_id": product["id"],
                    "quantity": quantity,
                    "total_amount": round(quantity * product["price"], 2),
                    "created_at": created_at,
                    "updated_at": created_at,
                }
            )

    return sales

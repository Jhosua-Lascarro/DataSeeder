import random

from dataseeder.utils.time import fake, random_past_datetime


def generate_products(user_ids: list[str], per_user: int = 5) -> list[dict]:
    """Generate a list of products given a list of user_ids."""

    products = []
    name_products = [
        "Notebook Pro 14",
        "Smartwatch Pulse X",
        "Auriculares WaveSound",
        "Teclado Mecánico Orion",
        "Mouse Inalámbrico Flux",
        "Monitor UltraView 27",
        "Cámara Web ClearCam HD",
        "Disco SSD NovaDrive 1TB",
        "Router AirLink AX3000",
        "Tablet CoreTab 10",
        "Altavoz Bluetooth BoomMini",
        "Micrófono StudioCast",
        "Laptop Stand ErgoLift",
        "Power Bank VoltMax 20000",
        "Cargador Rápido TurboCharge",
        "Cable USB-C FlexLine",
        "Silla Ergonómica WorkEase",
        "Lámpara LED DeskLight",
        "Mochila TechPack Pro",
        "Hub USB-C MultiPort",
    ]

    for user_id in user_ids:
        for _ in range(per_user):
            created_at = random_past_datetime()

            products.append(
                {
                    "user_id": user_id,
                    "name": random.choice(name_products),
                    "description": fake.sentence(),
                    "price": round(random.uniform(5, 500), 2),
                    "stock": random.randint(1, 100),
                    "image_url": fake.image_url(),
                    "created_at": created_at,
                    "updated_at": created_at,
                }
            )

    return products

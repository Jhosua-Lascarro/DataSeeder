from random import choice

from dataseeder.utils.time import fake, random_past_datetime

ROLES = ["client"]  # Admin
STATUS = ["active", "inactive"]


def generate_clients(user_ids: list[str]) -> list[dict]:
    """Generate a list of clients given a list of user_ids."""

    clients = []

    for user_id in user_ids:
        created_at = random_past_datetime()

        clients.append(
            {
                "user_id": user_id,
                "name": fake.name(),
                "email": fake.unique.email(),
                "phone": fake.phone_number(),
                "company": fake.company(),
                "role": choice(ROLES),
                "status": choice(STATUS),
                "created_at": created_at,
                "updated_at": created_at,
            }
        )

    return clients

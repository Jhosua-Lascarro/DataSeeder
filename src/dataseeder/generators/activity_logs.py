from random import choice

from dataseeder.utils.time import fake, random_past_datetime

TYPES = [
    "client_created",
    "product_created",
    "sale_created",
    "client_updated",
    "product_updated",
]

RESOURCE_TYPES = ["client", "product", "sale"]


def generate_activity_logs(
    user_ids: list[str], resources: list[dict], logs_per_user: int = 10
) -> list[dict]:
    """Generate a list of activity logs given a list of user_ids and resources."""

    logs = []

    for user_id in user_ids:
        for _ in range(logs_per_user):
            resource = choice(resources)
            created_at = random_past_datetime()

            logs.append(
                {
                    "user_id": user_id,
                    "type": choice(TYPES),
                    "description": fake.sentence(),
                    "resource_type": choice(RESOURCE_TYPES),
                    "resource_id": resource.get("id"),
                    "created_at": created_at,
                }
            )

    return logs

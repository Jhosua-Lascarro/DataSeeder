from faker import Faker

from dataseeder.supabase.config import settings
from dataseeder.supabase.db import supabase

fake = Faker()


def seed_auth_users(n: int = 5) -> list[str]:
    """Seed n authentication users into the database and return their user_ids."""

    user_ids = []

    for i in range(n):
        email = fake.unique.email()

        if settings.DRY_RUN:
            fake_id = f"dry-run-user-{i}"
            user_ids.append(fake_id)
            print(f"[DRY-RUN] auth.users: {email}")
            continue

        res = supabase.auth.admin.create_user(
            {"email": email, "password": "Password123!", "email_confirm": True}
        )

        user_ids.append(res.user.id)

    return user_ids

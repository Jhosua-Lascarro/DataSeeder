from uuid import uuid4

import pandas as pd

from dataseeder.generators.products import generate_products
from dataseeder.schemas.products import products_schema
from dataseeder.supabase.config import settings
from dataseeder.utils.insert import insert
from dataseeder.utils.schema import validate_df
from dataseeder.utils.serialize import serialize_for_supabase


def seed_products(user_ids: list[str], per_user: int = 5) -> list[dict]:
    """Seed products into the database for given user_ids."""

    df = pd.DataFrame(generate_products(user_ids, per_user))
    validate_df(df, products_schema)

    df = serialize_for_supabase(df)

    records = df.to_dict("records")

    if settings.DRY_RUN:
        # Assign random UUIDs for dry run
        for r in records:
            r["id"] = str(uuid4())
        print(f"[DRY-RUN] products: {len(records)} records to be inserted.")
        return records

    return insert("products", df.to_dict("records"))

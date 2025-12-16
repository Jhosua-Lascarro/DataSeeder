from uuid import uuid4

from pandas import DataFrame

from dataseeder.generators.clients import generate_clients
from dataseeder.schemas.clients import clients_schema
from dataseeder.supabase.config import settings
from dataseeder.utils.insert import insert
from dataseeder.utils.schema import validate_df
from dataseeder.utils.serialize import serialize_for_supabase


def seed_clients(user_ids: list[str]) -> list[dict]:
    """Seed clients into the database for given user_ids."""

    df = DataFrame(generate_clients(user_ids))

    validate_df(df, clients_schema)
    df = serialize_for_supabase(df)

    records = df.to_dict("records")

    if settings.DRY_RUN:
        # Assign random UUIDs for dry run
        for r in records:
            r["id"] = str(uuid4())
        print(f"[DRY-RUN] clients: {len(records)} records to be inserted.")
        return records

    return insert("clients", df.to_dict("records"))

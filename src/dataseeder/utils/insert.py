from dataseeder.supabase.config import settings
from dataseeder.supabase.db import supabase


def insert(table: str, records: list[dict]) -> list[dict]:
    """Try to insert records into a given table. If DRY_RUN is enabled, just print the action."""

    if settings.DRY_RUN:
        # Return the records as-is in dry-run mode
        print(f"[DRY-RUN] {table}: {len(records)} records to be inserted.")
        return records

    res = supabase.table(table).insert(records).execute()
    return res.data

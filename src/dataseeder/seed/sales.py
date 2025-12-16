from pandas import DataFrame

from dataseeder.generators.sales import generate_sales
from dataseeder.schemas.sales import sales_schema
from dataseeder.utils.insert import insert
from dataseeder.utils.schema import validate_df
from dataseeder.utils.serialize import serialize_for_supabase


def seed_sales(user_ids: list[str], products: list[dict]) -> list[dict]:
    """Seed sales into the database for given user_ids and products."""

    df = DataFrame(generate_sales(user_ids, products))
    validate_df(df, sales_schema)

    df = serialize_for_supabase(df)
    return insert("sales", df.to_dict("records"))

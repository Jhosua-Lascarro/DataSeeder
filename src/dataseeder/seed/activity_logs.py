from pandas import DataFrame

from dataseeder.generators.activity_logs import generate_activity_logs
from dataseeder.schemas.activity_logs import activity_logs_schema
from dataseeder.utils.insert import insert
from dataseeder.utils.schema import validate_df
from dataseeder.utils.serialize import serialize_for_supabase


def seed_activity_logs(user_ids, resources):
    df = DataFrame(generate_activity_logs(user_ids, resources))
    validate_df(df, activity_logs_schema)

    df = serialize_for_supabase(df)
    return insert("activity_logs", df.to_dict("records"))

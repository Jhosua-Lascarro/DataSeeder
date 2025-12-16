import pandas as pd


def serialize_for_supabase(df: pd.DataFrame) -> pd.DataFrame:
    """Serialize datetime columns in a DataFrame to ISO 8601 format for Supabase."""

    df = df.copy()

    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    return df

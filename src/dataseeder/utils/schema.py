from pandas import DataFrame
from pandera import DataFrameSchema


def validate_df(df: DataFrame, schema: DataFrameSchema) -> DataFrame:
    """Validate a DataFrame against a given schema."""

    schema.validate(df, lazy=True)
    return df

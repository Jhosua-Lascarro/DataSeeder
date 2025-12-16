from pandera import Check, Column
from pandera.pandas import DataFrameSchema, DateTime

sales_schema = DataFrameSchema(
    {
        "user_id": Column(str, nullable=False),
        "product_id": Column(str, nullable=False),
        "quantity": Column(
            int,
            nullable=False,
            checks=Check.gt(0),
        ),
        "total_amount": Column(
            float,
            nullable=False,
            checks=Check.gt(0),
        ),
        "created_at": Column(DateTime, nullable=False),
        "updated_at": Column(DateTime, nullable=False),
    },
    strict=True,
)

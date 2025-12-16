from pandera import Check, Column
from pandera.pandas import DataFrameSchema, DateTime

products_schema = DataFrameSchema(
    {
        "user_id": Column(str, nullable=False),
        "name": Column(str, nullable=False),
        "description": Column(str, nullable=True),
        "price": Column(
            float,
            nullable=False,
            checks=Check.gt(0),
        ),
        "stock": Column(
            int,
            nullable=False,
            checks=Check.ge(0),
        ),
        "image_url": Column(str, nullable=True),
        "created_at": Column(DateTime, nullable=False),
        "updated_at": Column(DateTime, nullable=False),
    },
    strict=True,
)

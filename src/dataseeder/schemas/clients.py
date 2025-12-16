from pandera import Check, Column
from pandera.pandas import DataFrameSchema, DateTime

clients_schema = DataFrameSchema(
    {
        "user_id": Column(str, nullable=False),
        "name": Column(str, nullable=False),
        "email": Column(
            str,
            nullable=False,
            checks=Check.str_matches(r".+@.+\..+"),
        ),
        "phone": Column(str, nullable=True),
        "company": Column(str, nullable=True),
        "role": Column(
            str,
            nullable=False,
            checks=Check.isin(["admin", "client"]),
        ),
        "status": Column(
            str,
            nullable=False,
            checks=Check.isin(["active", "inactive"]),
        ),
        "created_at": Column(DateTime, nullable=False),
        "updated_at": Column(DateTime, nullable=False),
    },
    strict=True,
)

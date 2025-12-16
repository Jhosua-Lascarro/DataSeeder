from pandera import Column
from pandera.pandas import DataFrameSchema, DateTime

activity_logs_schema = DataFrameSchema(
    {
        "user_id": Column(str, nullable=False),
        "type": Column(str, nullable=False),
        "description": Column(str, nullable=False),
        "resource_type": Column(str, nullable=True),
        "resource_id": Column(str, nullable=True),
        "created_at": Column(DateTime, nullable=False),
    },
    strict=True,
)

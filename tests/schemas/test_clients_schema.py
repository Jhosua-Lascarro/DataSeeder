from uuid import uuid4

from faker import Faker
from pandas import DataFrame
from pandera.errors import SchemaError
from pytest import raises

from dataseeder.schemas.clients import clients_schema

fake = Faker("en_US")

df = DataFrame(
    [
        {
            "user_id": str(uuid4()),
            "name": "John",
            "email": "john@test.com",
            "phone": "123456789",
            "company": "ACME",
            "role": "admin",
            "status": "active",
            "created_at": fake.date_time_between(start_date=f"-{90}d", end_date="now"),
            "updated_at": fake.date_time_between(start_date=f"-{90}d", end_date="now"),
        }
    ]
)


def test_client_valid():
    validated_df = clients_schema.validate(df)
    assert not validated_df.empty


def test_client_invalit():
    df_invalid = df.copy()
    df_invalid.loc[0, "email"] = "invalid_email"
    df_invalid.loc[0, "role"] = "guest"  # No permitido
    with raises(SchemaError):
        clients_schema.validate(df_invalid)

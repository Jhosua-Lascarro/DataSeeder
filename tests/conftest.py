from uuid import uuid4

from faker import Faker
from pytest import fixture


@fixture
def fake():
    return Faker()


@fixture
def user_ids():
    return [str(uuid4()) for _ in range(3)]

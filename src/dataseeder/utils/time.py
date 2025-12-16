from faker import Faker

fake = Faker("en_US")


def random_past_datetime(days: int = 90):
    """Generate a random past datetime within the last `days` days."""

    return fake.date_time_between(start_date=f"-{days}d", end_date="now")

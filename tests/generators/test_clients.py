from dataseeder.generators.clients import generate_clients


def test_generate_clients_count(user_ids):
    data = generate_clients(user_ids)
    assert len(data) == len(user_ids)


def test_generate_clients_shape(user_ids):
    client = generate_clients(user_ids)[0]

    required_fields = {
        "user_id",
        "name",
        "email",
        "phone",
        "company",
        "role",
        "status",
        "created_at",
        "updated_at",
    }

    assert required_fields.issubset(client.keys())

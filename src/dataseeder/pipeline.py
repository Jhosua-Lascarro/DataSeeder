from dataseeder.seed.activity_logs import seed_activity_logs
from dataseeder.seed.auth import seed_auth_users
from dataseeder.seed.clients import seed_clients
from dataseeder.seed.products import seed_products
from dataseeder.seed.sales import seed_sales
from dataseeder.supabase.config import settings

def runner(n: int = settings.RECORDS):
    if settings.SUPABASE_URL == "https://supabase_url.supabase" or settings.SUPABASE_SERVICE_ROLE_KEY == "service_key":
        raise ValueError("ERROR: Please set your SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in the .env file.")
    
    print("Starting seed pipeline")
    print(f"Dry run: {settings.DRY_RUN}")
    print("-" * 40)

    # 1️⃣ auth.users
    print("Seeding auth users...")

    user_ids = seed_auth_users(n)
    print(f"   -> created {len(user_ids)} users")

    # 2️⃣ clients
    print("Seeding clients...")
    clients = seed_clients(user_ids)
    print(f"   -> inserted {len(clients)} clients")

    # 3️⃣ products
    print("Seeding products...")
    products = seed_products(user_ids)
    print(f"   -> inserted {len(products)} products")

    # 4️⃣ sales
    print("Seeding sales...")
    sales = seed_sales(user_ids, products)
    print(f"   -> inserted {len(sales)} sales")

    # 5️⃣ activity logs
    print("Seeding activity logs...")
    logs = seed_activity_logs(user_ids, clients + products + sales)
    print(f"   -> inserted {len(logs)} logs")

    print("-" * 40)
    print("Seed pipeline finished")


if __name__ == "__main__":
    runner()

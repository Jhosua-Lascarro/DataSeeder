from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SUPABASE_URL: str = "https://supabase_url.supabase"
    SUPABASE_SERVICE_ROLE_KEY: str = "service_key"
    RECORDS: int = 200
    DRY_RUN: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

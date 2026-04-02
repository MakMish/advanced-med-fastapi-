from pydantic_settings import BaseSettings, SettingsConfigDict

class setting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    cloud_name: str
    api_key: str
    api_secret: str
    url: str
    SECRET_KEY : str
    ALGORITHM : str
    
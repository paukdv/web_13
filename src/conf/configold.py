from pydantic_settings import BaseSettings
# from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    secret_key_jwt: str
    algorithm: str
    mail_username: str
    mail_password: str = "zukvov-cukzy9-xAwfob"
    # mail_from: str = "paukdv@meta.ua"
    mail_from: str
    mail_port: int = 465
    mail_server: str = "smtp.meta.ua"
    redis_host: str = "localhost"
    redis_port: int = 6379

    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

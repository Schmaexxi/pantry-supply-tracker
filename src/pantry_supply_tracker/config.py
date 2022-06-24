from pydantic import BaseSettings


class Settings(BaseSettings):

    host_port: int
    server_port: int

    class Config:
        env_file = ".env"


app_config = Settings()

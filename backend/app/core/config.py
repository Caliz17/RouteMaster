import os

class Settings:
    PROJECT_NAME: str = "RouteMaster"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # por ahora sqlite

settings = Settings()

import os
class Config:
    TESTING = True
    DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:5432/{}".format(
        os.environ.get("DB_USERNAME", "postgres"),
        os.environ.get("DB_PASSWORD", ""),
        os.environ.get("DB_HOST", "0.0.0.0"),
        os.environ.get("DB_NAME", "postgres")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
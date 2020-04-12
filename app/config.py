class Config:
    TESTING = True
    DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:@0.0.0.0:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
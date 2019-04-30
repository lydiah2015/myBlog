import os

class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL","postgres+psycopg2://postgres:p@127.0.0.1:5432/blog")
    SECRET_KEY=os.environ.get("SECRET_KEY","super secret key")
    WRITER_USERNAME=os.environ.get("WRITER_USERNAME","writer")
    WRITER_PASSWORD=os.environ.get("WRITER_PASSWORD","writer")


class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options={
    "development":DevConfig,
    "production":ProdConfig,
    "test":TestConfig,
}
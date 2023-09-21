import databases
import sqlalchemy
from sqlalchemy import ForeignKey
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("username", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(128)),)

products = sqlalchemy.Table("products",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("description", sqlalchemy.String(128)),
                         sqlalchemy.Column("price", sqlalchemy.String(128)),)

orders = sqlalchemy.Table("orders",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("users.id")),
                         sqlalchemy.Column("product_id", sqlalchemy.Integer, ForeignKey("products.id")),
                         sqlalchemy.Column("date", sqlalchemy.String(128)),
                         sqlalchemy.Column("status", sqlalchemy.String(128)),)


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

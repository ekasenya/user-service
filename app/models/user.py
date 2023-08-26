from sqlalchemy import String, Table, Column, Integer

from .metadata import metadata


user_account = Table(
    "user_account",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("email", String),

)

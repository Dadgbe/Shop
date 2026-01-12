from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
)
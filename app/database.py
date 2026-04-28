# Imports SQLAlchemy tools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file in project root.
# "./" means current directory.
DATABASE_URL = "sqlite:///./restaurant.db"

# Creates actual database engine.
# Engine = connection manager.
engine = create_engine(
    DATABASE_URL,

    # Needed specifically for SQLite.
    connect_args={"check_same_thread": False}
)

# Creates sessions.
# Session = conversation with database.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class every model inherits from.
# Think "template for database tables"
Base = declarative_base()

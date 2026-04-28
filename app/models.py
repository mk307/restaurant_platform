from sqlalchemy import (
Column,
Integer,
String,
DateTime
)

from app.database import Base


# Reservation table
class Reservation(Base):

    # SQL table name
    __tablename__ = "reservations"

    # Primary key
    id = Column(
        Integer,
        primary_key=True
    )

    customer_name = Column(String)

    party_size = Column(Integer)

    reservation_time = Column(DateTime)

    status = Column(
        String,
        default="Booked"
    )


# Restaurant tables entity
class Table(Base):

    __tablename__="tables"

    id=Column(
      Integer,
      primary_key=True
    )

    table_number=Column(Integer)

    capacity=Column(Integer)

    availability=Column(
      String,
      default="Available"
    )

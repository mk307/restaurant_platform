from pydantic import BaseModel
from datetime import datetime


class ReservationCreate(
BaseModel
):

    # User must send string
    customer_name:str

    # Must send integer
    party_size:int

    # Must be datetime
    reservation_time:datetime


class TableCreate(
BaseModel
):

    table_number:int

    capacity:int

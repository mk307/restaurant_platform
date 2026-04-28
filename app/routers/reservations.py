from fastapi import (
APIRouter,
Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app import crud,schemas


router=APIRouter(
prefix="/reservations",
tags=["Reservations"]
)


# Dependency injection.
# Opens database session.
def get_db():

    db=SessionLocal()

    try:
       yield db

    finally:
       db.close()


# POST endpoint
@router.post("/")
def create_reservation(
reservation:
schemas.ReservationCreate,

db:Session=
Depends(get_db)
):

 return crud.create_reservation(
   db,
   reservation
 )


# GET endpoint
@router.get("/")
def list_reservations(
db:Session=
Depends(get_db)
):

 return crud.get_reservations(db)

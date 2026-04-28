from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud,schemas

router=APIRouter(prefix="/tables",tags=["Tables"])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_table(
table:schemas.TableCreate,
db:Session=Depends(get_db)
):
    return crud.create_table(db,table)


@router.get("/")
def list_tables(
db:Session=Depends(get_db)
):
    return crud.get_tables(db)
    
@router.get("/available")
def available_tables(
db: Session = Depends(get_db)
):
    return db.query(
       models.Table
    ).filter(
       models.Table.availability=="Available"
    ).all()

from app import models


# CREATE reservation

def create_reservation(
db,
reservation
):

    # Convert API data into model object
    r=models.Reservation(
      **reservation.dict()
    )

    # Add to session
    db.add(r)

    # Save permanently
    db.commit()

    # Reload with generated ID
    db.refresh(r)

    return r


# READ reservations

def get_reservations(db):

    return db.query(
      models.Reservation
    ).all()


# CREATE tables

def create_table(
db,
table
):

    t=models.Table(
      **table.dict()
    )

    db.add(t)

    db.commit()

    db.refresh(t)

    return t


# READ tables

def get_tables(db):

    return db.query(
       models.Table
    ).all()

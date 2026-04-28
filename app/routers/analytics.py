from fastapi import APIRouter

router=APIRouter(
prefix="/analytics",
tags=["Analytics"]
)


@router.get(
"/dashboard"
)
def dashboard():

 return {
   "today_reservations":22,
   "occupancy_rate":"81%",
   "peak_hour":"19:00"
 }

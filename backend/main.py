from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Reservation, Base
from database import engine, SessionLocal
from schemas import ReservationCreate, ReservationOut
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.post("/reservations/", response_model=ReservationOut)
def create_reservation(reservation: ReservationCreate):
    db = SessionLocal()
    db_res = Reservation(**reservation.dict())
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    db.close()
    return db_res

@app.get("/reservations/", response_model=list[ReservationOut])
def get_reservations():
    db = SessionLocal()
    res_list = db.query(Reservation).all()
    db.close()
    return res_list

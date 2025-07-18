from pydantic import BaseModel

class ReservationCreate(BaseModel):
    name: str
    email: str
    suite: str
    date: str

class ReservationOut(ReservationCreate):
    id: int

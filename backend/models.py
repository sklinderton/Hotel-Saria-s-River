from sqlalchemy import Column, Integer, String
from database import Base

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    suite = Column(String(100))
    date = Column(String(20))

from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class Banks(Base):
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)


class Branches(Base):
    __tablename__ = "branches"

    ifsc = Column(String,index=True, primary_key=True)
    bank_id = Column(Integer, ForeignKey("banks.id"))
    branch = Column(String,index=True)
    address = Column(String,index=True)
    city = Column(String,index=True)
    district = Column(String,index=True)
    state = Column(String,index=True)


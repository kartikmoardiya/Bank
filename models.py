from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Bank(Base):
    __tablename__ = "bank"

    Account_Number = Column(Integer, primary_key = True, nullable = False)
    Pin = Column(Integer, nullable = False)
    Balance = Column(Integer, nullable = False, default=0)
    Prefix = Column(String, nullable = False)
    First_Name = Column(String, nullable = False)
    Middle_Name = Column(String, nullable = False)
    Last_Name = Column(String, nullable = False)
    Area = Column(String, nullable = False)
    City = Column(String, nullable = False)
    State = Column(String, nullable = False)
    Country = Column(String, nullable = False, default = "India")
    Zipcode = Column(Integer, nullable = False)
    Phone_Number = Column(Integer, nullable = False)
    Date_Of_Birth = Column(String, nullable = False)
    Maritual_Status = Column(Boolean, nullable = False)
    Occuoation = Column(String, nullable = False)
    Aadhar_Card_Number = Column(Integer, nullable = False)
    Email = Column(String, nullable = False)
    Gender = Column(String, nullable = False)
    Account_Tyoe = Column(String, nullable = False)
    create_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('now()'))
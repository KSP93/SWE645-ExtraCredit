from sqlalchemy import Column, Integer, String, Date, Enum
from app.core.database import Base

class Survey(Base):
    __tablename__ = "surveys"

    id            = Column(Integer, primary_key=True, index=True)
    first_name    = Column(String(50), index=True, nullable=False)
    last_name     = Column(String(50), nullable=False)
    email         = Column(String(120), nullable=False, unique=True)
    street        = Column(String(120))
    city          = Column(String(80))
    state         = Column(String(2))
    zip           = Column(String(12))
    phone         = Column(String(20))
    date_of_survey= Column(Date)
    liked_most    = Column(String(120))        # free-text or CSV
    interested_in = Column(String(120))
    likelihood    = Column(Enum("Very Likely", "Likely", "Unlikely", name="likelihood_enum"))

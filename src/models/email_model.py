from sqlalchemy import Column, INTEGER, VARCHAR, TEXT
from src.models.base_model import BaseModel

class Email(BaseModel):
    __tablename__ = "emails"

    id_email = Column(INTEGER, primary_key=True, autoincrement=True)
    subject = Column(VARCHAR(255), nullable=False)
    body_email = Column(TEXT, nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    name_employee = Column(VARCHAR(255), nullable=False)
    position_employee = Column(VARCHAR(255), nullable=False)



from src.models.email_model import Email
from typing import List
from sqlalchemy.orm import Session
from src.exceptions import EntityValidationError, NotFoundError

class EmailRepositorie:
    def __init__(self, session: Session):
        self.session = session

    def create(
        self, 
        subject: str,
        body_email: str,
        email_destiny: str,
        name_employee: str,
        position_employee: str
    ) -> Email:
        email = Email(
            email=email_destiny,
            subject=subject,
            body_email=body_email,
            name_employee=name_employee,
            position_employee=position_employee
        )

        self.session.add(email)
        self.session.commit()
        return email
    
    def select_all(self) -> List[Email]:
        return self.session.query(Email).all()
    
    def select(self, id_email: int) -> Email:
        email = self.session.query(Email).filter(Email.id_email == id_email).first()

        if email is None:
            raise NotFoundError("Não foi encontrado nenhum e-mail referente ao ID.")

        return email
    
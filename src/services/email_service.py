from src.config.constants import session
from src.repositories.email_repositorie import EmailRepositorie
from src.dto.email_dtos import EmailCreateDTO, EmailFilterDTO, EmailResponseDTO
from typing import List

class EmailService:
    def __init__(self):
        self.__email_repositorie = EmailRepositorie(session=session)

    def create(self, email_create_dto: EmailCreateDTO) -> EmailResponseDTO:
        email = self.__email_repositorie.create(
            subject=email_create_dto.subject,
            body_email=email_create_dto.body_email,
            email_destiny=email_create_dto.email,
            name_employee=email_create_dto.name_employee,
            position_employee=email_create_dto.position_employee
        )

        email_response_dto = EmailResponseDTO(
            id_email=email.id_email,
            subject=email.subject,
            email=email.email,
            body_email=email.body_email,
            name_employee=email.name_employee,
            position_employee=email.position_employee
        )

        return email_response_dto

    def select_all(self) -> List[EmailResponseDTO]:  
        emails_response_dto = []

        for email in self.__email_repositorie.select_all():
            email_response = EmailResponseDTO(
                id_email=email.id_email,
                subject=email.subject,
                body_email=email.body_email,
                name_employee=email.name_employee,
                position_employee=email.position_employee
            ) 
            emails_response_dto.append(email_response)
            
        return emails_response_dto  

    def select(self, email_filter_dto: EmailFilterDTO) -> EmailResponseDTO:  
        email = self.__email_repositorie.select(
            id_email=email_filter_dto.id_email
        )

        email_response = EmailResponseDTO(
            id_email=email.id_email,
            subject=email.subject,
            body_email=email.body_email,
            name_employee=email.name_employee,
            position_employee=email.position_employee
        ) 
        return email_response  

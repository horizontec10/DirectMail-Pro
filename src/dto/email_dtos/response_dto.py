from pydantic import BaseModel

class EmailResponseDTO(BaseModel):
    
    id_email: int
    subject: str
    body_email: str
    email: str
    name_employee: str
    position_employee: str


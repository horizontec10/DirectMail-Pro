from pydantic import BaseModel, field_validator
from src.exceptions import UnprocessableEntity, InvalidFields

class EmailCreateDTO(BaseModel):
    
    subject: str
    body_email: str
    email: str
    name_employee: str
    position_employee: str


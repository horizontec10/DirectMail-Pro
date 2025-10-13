from pydantic import BaseModel, field_validator
from src.exceptions import UnprocessableEntity, InvalidFields

class EmailFilterDTO(BaseModel):
    
    id_email: int

    

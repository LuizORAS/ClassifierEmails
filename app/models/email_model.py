from pydantic import BaseModel

class EmailCredentials(BaseModel):
    username: str
    password: str
    emails_number: int
    days: int
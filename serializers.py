from pydantic import BaseModel


class Bank(BaseModel):

    id: int
    name: str

class Branches(BaseModel):

    ifsc: str
    bank_id: Bank.id
    branch: str
    address: str
    city: str
    district: str
    state: str
    
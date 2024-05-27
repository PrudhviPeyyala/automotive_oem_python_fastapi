from pydantic import BaseModel


class AutoOem(BaseModel):
    manufacturer: str
    oemModel: str
    yearModel: int
    origin: str

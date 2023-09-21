from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    description: str
    price: float


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

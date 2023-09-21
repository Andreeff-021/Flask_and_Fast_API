from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Status(Enum):
    IN_PROCESSING = "в обработке"
    READY = "готов"


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date: str = datetime.now().replace(microsecond=0)
    status: str = Status.IN_PROCESSING


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    date: str
    status: str

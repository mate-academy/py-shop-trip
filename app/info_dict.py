from dataclasses import dataclass

from app.customer import Customer
from app.shop import Shop


@dataclass
class InfoDict:
    customers: list[Customer]
    shops: list[Shop]
    fuel_price: float

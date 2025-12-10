from dataclasses import dataclass


@dataclass
class Purchase:
    product: str
    quantity: int
    total_price: float

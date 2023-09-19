from dataclasses import dataclass


@dataclass
class DayMark:
    fuel_price: int | float
    date: str

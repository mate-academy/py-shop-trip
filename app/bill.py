from dataclasses import dataclass, field

from app.shop import Shop


@dataclass
class Bill:
    recipe: dict
    travel_cost: float
    recipe_price: float
    shop: Shop
    total_price: float = field(init=False)

    def __post_init__(self) -> None:
        self.total_price = round(self.travel_cost + self.recipe_price, 2)

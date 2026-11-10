from dataclasses import dataclass

from app.models.customer.customer import Customer
from app.models.shop.shop import Shop


@dataclass
class ShoppingResult:
    customer: Customer
    shopping_options: dict[str, int | float]
    lowest_total_cost_shop: Shop | None
    money_after_purchase: int | float

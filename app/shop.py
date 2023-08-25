import dataclasses
from typing import Dict
from decimal import Decimal


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: Dict[str, Decimal]

    def customer_total_price(
            self,
            customer_product_dict: dict
    ) -> Decimal:
        return Decimal(sum(
            customer_product_dict[item] * self.products[item]
            for item in customer_product_dict.keys()
        ))

import dataclasses
from typing import Any


@dataclasses.dataclass
class Shop:
    name: str
    location: tuple
    products: dict

    def prod_price(self) -> Any:
        return self.products.values()

from typing import List, Union, Dict


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: Union[int, float],
            car: Dict[str, Union[str, float]]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return f"{self.name}"

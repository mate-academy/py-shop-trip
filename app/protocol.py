from typing import Protocol


class ShopProtocol(Protocol):
    name: str
    location: list[int]
    products: dict[str, int | float]

    def check_products(self, cart: dict[str, int]) -> bool:
        ...

    def buy_products(self, customer: "CustomerProtocol") -> None:
        ...


class CustomerProtocol(Protocol):
    name: str
    product_cart: dict[str, float | int]
    location: list[int]
    money: int
    car: "CarProtocol"

    def calc_trip_cost(self, shop: "ShopProtocol", fuel_price: float) -> float:
        ...


class CarProtocol(Protocol):
    brand: str
    fuel_consumption: float

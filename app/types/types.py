from typing import TypedDict


class CarData(TypedDict):
    brand: str
    fuel_consumption: float


class CustomerData(TypedDict):
    name: str
    product_cart: dict[str, int]
    location: tuple[int, int]
    money: float
    car: CarData


class ShopData(TypedDict):
    name: str
    location: tuple[int, int]
    products: dict[str, float]


class ConfigData(TypedDict):
    FUEL_PRICE: float
    customers: list[CustomerData]
    shops: list[ShopData]

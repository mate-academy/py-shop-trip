from __future__ import annotations
from dataclasses import dataclass
from app.location import Location
from app.car import Car


@dataclass
class Order:
    product: Product
    amount: int

    @classmethod
    def deserialize_from_dict(cls, info: dict) -> list[Order]:
        return [
            cls(Product(key, 0), value) for key, value in info.items()
        ]


@dataclass
class Product:
    name: str
    price: float

    @classmethod
    def deserialize_from_dict(cls, info: dict) -> dict[str, Product]:
        return {
            key: cls(key, value) for key, value in info.items()
        }


@dataclass
class Shop:
    name: str
    products: dict[str, Product]
    location: Location

    @classmethod
    def deserialize_from_dict(cls, info: dict) -> Shop:
        return cls(
            name=info["name"],
            products=Product.deserialize_from_dict(info["products"]),
            location=Location.deserialize_from_list(info["location"]),
        )

    def get_total_cost(self, customer: Customer) -> float:
        total = 0
        for item in customer.orders:
            total += item.amount * self.products.get(item.product.name).price
        return total


@dataclass
class Customer:
    name: str
    orders: list[Order]
    location: Location
    money: float
    car: Car

    @classmethod
    def deserialize_from_dict(cls, info: dict) -> Customer:
        return cls(
            name=info["name"],
            orders=Order.deserialize_from_dict(info["product_cart"]),
            location=Location.deserialize_from_list(info["location"]),
            money=info["money"],
            car=Car.deserialize_from_dict(info["car"])
        )

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        return round(
            (self.location.find_distance(shop.location)
             * self.car.fuel_consumption * fuel_price / 100) * 2, 2
        )

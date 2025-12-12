import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_data() -> dict:
    path = Path(__file__).resolve().parent / "config.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_objects(data: dict) -> tuple[float, list[Customer], list[Shop]]:
    fuel_price = float(data["FUEL_PRICE"])

    shops = [
        Shop(
            name=s["name"],
            location=[float(s["location"][0]), float(s["location"][1])],
            products={k: float(v) for k, v in s["products"].items()},
        )
        for s in data["shops"]
    ]

    customers = []
    for cust in data["customers"]:
        car = Car(
            brand=cust["car"]["brand"],
            fuel_consumption=float(cust["car"]["fuel_consumption"]),
        )
        customers.append(
            Customer(
                name=cust["name"],
                product_cart={
                    k: int(v) for k, v in cust["product_cart"].items()},
                location=[
                    float(cust["location"][0]), float(cust["location"][1])],
                money=float(cust["money"]),
                car=car,
            )
        )

    return fuel_price, customers, shops

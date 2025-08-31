import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def _load_config() -> dict:
    cfg_path = Path(__file__).resolve().parent / "config.json"
    with cfg_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_info_from_json() -> tuple[float, list[Customer], list[Shop]]:
    config = _load_config()
    fuel_price: float = float(config["FUEL_PRICE"])

    customers: list[Customer] = []
    for record in config["customers"]:
        car = Car(
            brand=record["car"]["brand"],
            fuel_consumption=float(record["car"]["fuel_consumption"]),
        )
        cust = Customer(
            name=record["name"],
            product_cart={k: int(v) for k, v in record["product_cart"].items()},
            location=[(record["location"][0]), (record["location"][1])],
            money=record["money"],
            car=car,
        )
        customers.append(cust)

    shops: list[Shop] = []
    for record in config["shops"]:
        shop = Shop(
            name=record["name"],
            location=[(record["location"][0]), (record["location"][1])],
            products={k: float(v) for k, v in record["products"].items()},
        )
        shops.append(shop)

    return fuel_price, customers, shops
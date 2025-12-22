import json
from app.car import CarInfo
from app.shop import ShopInfo
from app.customers import CustomerInfo
from pathlib import Path
from app.calculation import calc


def shop_trip() -> None:
    buyers = []
    shops = []
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        for customer in config["customers"]:
            car = customer.get("car")
            buyers.append(CustomerInfo(customer["name"],
                                       customer["product_cart"],
                                       customer["location"],
                                       customer["money"],
                                       CarInfo(car["brand"],
                                               car["fuel_consumption"],
                                               config["FUEL_PRICE"])))
        for shop in config["shops"]:
            shops.append(ShopInfo(shop["name"],
                                  shop["location"],
                                  shop["products"]))

    result = calc(shops, buyers)
    print(result)

import json
from app.customer import Customer
from app.shops import Shop
from app.trip import Choose


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    buyers = [Customer(person) for person in config["customers"]]
    shops = [Shop(market) for market in config["shops"]]

    for person in buyers:
        person.petrol_today = fuel_price

    for person in buyers:
        Choose(person, shops).get_best_market()

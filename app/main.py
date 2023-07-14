import json

from app.cost_calculation import CostCalculation
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    customers = {}
    shops = {}

    source = "config.json"
    data = None

    with open(source, "r") as file:  # read
        data = json.load(file)

    for customer in data["customers"]:
        customers[f"{customer['name']}"] = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=customer["car"]
        )

    for shop in data["shops"]:
        shops[f"{shop['name']}"] = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )

    expense_counting_session = CostCalculation(
        customers, shops, data["FUEL_PRICE"]
    )
    calculations = expense_counting_session.calculation()

    for customer, shop in calculations.items():
        print(customer, shop)
        print(type(customer), type(shop))


if __name__ == "__main__":
    shop_trip()

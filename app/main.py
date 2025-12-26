import json


from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

    fuel_price: float = data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in data.get("customers")]
    shops = [Shop(shop) for shop in data.get("shops")]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = customer.get_cheapest_shop(fuel_price, shops)

        if best_shop:
            customer.ride_to_shop(fuel_price, best_shop)
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )

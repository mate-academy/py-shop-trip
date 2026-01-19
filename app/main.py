from json import load
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json") as config:
        data = load(config)

    fuel_price = data["FUEL_PRICE"]

    for customer in data["customers"]:
        current_customer = Customer(*customer.values())
        shops = [Shop(*shop.values()) for shop in data["shops"]]
        shop, cheapest_trip = current_customer.cheapest_trip(shops, fuel_price)

        if cheapest_trip > current_customer.money:
            print(f"{current_customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{current_customer.name} rides to {shop.name}\n")
            shop.shopping(current_customer.name, current_customer.product_cart)
            current_customer.return_home(cheapest_trip)

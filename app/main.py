import json
from app.customer import Customer
from app.shop import Shop


with open("app/config.json", "r") as f:
    data = json.load(f)


def shop_trip() -> None:
    fuel_price = data["FUEL_PRICE"]
    customers_dict = data["customers"]
    customers = []
    for customer in customers_dict:
        customers.append(Customer(customer["name"], customer["product_cart"],
                                  customer["location"], customer["money"],
                                  customer["car"]))
    shops_dict = data["shops"]
    shops = []
    for shop in shops_dict:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))
    for customer in customers:
        customer.make_choice(fuel_price, shops)


if __name__ == "__main__":
    shop_trip()

import json
from app.shop import Shop
from app.customer import Customer
from app.utils import choose_cheapest_shop


def shop_trip() -> None:
    with open("app/config.json") as f:
        data = json.load(f)

    shops = []
    for shop_data in data["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"],
        )
        shops.append(shop)

    customers = []
    for c_data in data["customers"]:
        customer = Customer(
            name=c_data["name"],
            product_cart=c_data["product_cart"],
            location=c_data["location"],
            money=c_data["money"],
            car_data=c_data["car"],
        )
        customers.append(customer)

    for customer in customers:
        cheapest_shop, cheapest_cost = choose_cheapest_shop(
            customer,
            shops,
            data["FUEL_PRICE"]
        )
        if customer.money < cheapest_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue

        customer.ride_to(cheapest_shop)
        customer.buy_products(cheapest_shop, data["FUEL_PRICE"])

        customer.ride_home()
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()

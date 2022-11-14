import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customer_data = []
    shop_data = []
    with open("app/config.json", "r") as data_source:
        data = json.load(data_source)
        for customer in data["customers"]:
            customer_data.append(Customer(customer))
        for shop in data["shops"]:
            shop_data.append(Shop(shop))
        with open("settings.json", "w") as file:
            json.dump({"Fuel_price": data["FUEL_PRICE"]}, file)

    for customer in customer_data:
        print(f"{customer.name} has {customer.money} dollars")
        enough_money_to_trip = {}
        for shop in shop_data:
            trip_cost = (customer.cost_trip_to(shop) * 2
                         + customer.cost_purchase_product(shop))
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")
            if trip_cost <= customer.money:
                enough_money_to_trip[trip_cost] = shop
        if enough_money_to_trip:
            shop = enough_money_to_trip[min(enough_money_to_trip)]
            customer.ride_to(shop)
            shop.print_purchase(customer.name, customer.product_cart)
            customer.rides_home()
            print(f"{customer.name} now has "
                  f"{round(customer.money - min(enough_money_to_trip), 2)}"
                  f" dollars\n")

        else:
            print(f"{customer.name} doesn't have enough money to "
                  f"make purchase in any shop")

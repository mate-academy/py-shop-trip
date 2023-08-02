import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop
import datetime


def shop_trip():
    with open("app/config.json") as f:
        config_data = json.load(f)
        fuel_price = config_data["FUEL_PRICE"]
        customers_data = config_data["customers"]
        shops_data = config_data["shops"]

    shops = []
    for shop_data in shops_data:
        shop = Shop(shop_data["name"], shop_data["location"], shop_data["products"])
        shops.append(shop)

    customers = []
    for customer_data in customers_data:
        car = Car(customer_data["car"]["brand"], customer_data["car"]["fuel_consumption"])
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            car
        )
        customers.append(customer)

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        min_trip_cost = float('inf')

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to {shop.name} costs {trip_cost:.2f}")
            if trip_cost < min_trip_cost and trip_cost <= customer.money:
                cheapest_shop = shop
                min_trip_cost = trip_cost

        if cheapest_shop is not None:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.money -= min_trip_cost
            current_time = datetime.datetime.now()
            cheapest_shop.print_purchase_receipt(customer, current_time)
            print(f"{customer.name} rides home")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        print(f"{customer.name} now has {customer.money:.2f} dollars")


if __name__ == "__main__":
    shop_trip()
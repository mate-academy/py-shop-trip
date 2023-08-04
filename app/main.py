import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop
from datetime import datetime


def shop_trip():
    with open("app/config.json") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    customers_data = config_data["customers"]
    shops_data = config_data["shops"]

    shops = [Shop(shop["name"], shop["location"], shop["products"]) for shop in shops_data]

    for customer_data in customers_data:
        customer_name = customer_data["name"]
        product_cart = customer_data["product_cart"]
        location = customer_data["location"]
        money = customer_data["money"]
        car_data = customer_data["car"]
        car_brand = car_data["brand"]
        fuel_consumption = car_data["fuel_consumption"]

        car = Car(car_brand, fuel_consumption)
        customer = Customer(customer_name, product_cart, location, money, car)

        cheapest_shop = None
        cheapest_trip_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            if trip_cost < cheapest_trip_cost and trip_cost <= customer.money:
                cheapest_shop = shop
                cheapest_trip_cost = trip_cost

        if cheapest_shop:
            print(f"{customer.name} has {customer.money} dollars")
            print(f"{customer.name}'s trip to {cheapest_shop.name} costs {cheapest_trip_cost:.2f}")
            customer.update_money(cheapest_trip_cost)
            print(f"{customer.name} rides to {cheapest_shop.name}")

            purchase_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            cheapest_shop.print_receipt(customer, purchase_time)

            customer.location = cheapest_shop.location

            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"\n{customer.name} doesn't have enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
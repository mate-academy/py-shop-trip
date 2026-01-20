import json
import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop

with open("app/config.json") as config:
    data = json.load(config)

customers = []
for customer_data in data["customers"]:
    car_data = customer_data.pop("car")
    car = Car(**car_data)
    customer = Customer(car=car, **customer_data)
    customers.append(customer)

shops = [Shop(**shop_data) for shop_data in data["shops"]]

fuel_price = data["FUEL_PRICE"]


def find_nearest_shop(customer: Customer,
                      shops: list,
                      fuel_price: float) -> tuple:
    min_cost = float("inf")
    nearest_shop = None
    costs = []
    for shop in shops:
        trip_cost = customer.cost_to_shop(shop.location, fuel_price, shop)
        costs.append((shop.name, trip_cost))
        if trip_cost < min_cost:
            min_cost = trip_cost
            nearest_shop = shop
    return nearest_shop, min_cost, costs


def shop_trip() -> None:
    for customer in customers:
        nearest_shop, min_cost, costs = (
            find_nearest_shop(customer, shops, fuel_price))
        print(f"{customer.name} has {customer.money} dollars")
        for shop_name, trip_cost in costs:
            print(f"{customer.name}'s trip to the "
                  f"{shop_name} costs {trip_cost:.2f}")

        product_cost = 0
        for product, quantity in customer.product_cart.items():
            product_cost += nearest_shop.products[product] * quantity

        if customer.money < min_cost + product_cost:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {nearest_shop.name}")
        home_location = customer.location
        customer.location = nearest_shop.location
        print()

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        def format_float(number: float) -> str:
            formatted_number = (("{:.2f}".format(number))
                                .rstrip("0").rstrip("."))
            return formatted_number

        for product, quantity in customer.product_cart.items():
            total_price = nearest_shop.products[product] * quantity
            formatted_price = format_float(total_price)
            print(f"{quantity} {product}s for {formatted_price} dollars")

        print(f"Total cost is {product_cost} dollars")
        print("See you again!")
        print()

        customer.money -= min_cost

        print(f"{customer.name} rides home")
        customer.location = home_location
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()


if __name__ == "__main__":
    shop_trip()

import json
import datetime
from pathlib import Path
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    config_path = base_dir / "config.json"

    with open(config_path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [Shop(shop_data["name"],
                  shop_data["location"],
                  shop_data["products"])
             for shop_data in data["shops"]]

    customers = []
    for car_data in data["customers"]:
        car = Car(
            car_data["car"]["brand"],
            car_data["car"]["fuel_consumption"])
        cust = Customer(
            car_data["name"],
            car_data["product_cart"],
            car_data["location"],
            car_data["money"], car)
        customers.append(cust)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = {}
        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            trip_costs[shop] = cost
            print(f"{customer.name}'shop_data trip to the "
                  f"{shop.name} costs {cost}")

        best_shop = min(trip_costs, key=trip_costs.get)

        shopping_cost = best_shop.calculate_cost(customer.product_cart)

        if trip_costs[best_shop] <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}")

            customer.location = best_shop.location
            customer.money -= trip_costs[best_shop]

            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"# Date: {now}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for item, quantity in customer.product_cart.items():
                price = best_shop.products[item]
                print(f"{quantity} {item} for {quantity * price} dollars")

            print(f"Total cost is {shopping_cost} dollars")
            print("See you again!")
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()

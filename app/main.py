from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app import parsing

from decimal import Decimal
import datetime


def shop_trip() -> None:
    config = parsing.parse_data_from_json()
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = []
    shops = []

    for customer_data in customers_data:
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            Decimal(customer_data["money"]),
            car
        )
        customers.append(customer)

    for shop_data in shops_data:
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_shop = None
        cheapest_cost = Decimal("inf")

        for shop in shops:
            fuel_cost = customer.calculate_fuel_cost(customer.car, shop)
            product_cost = customer.calculate_product_cost(shop)
            total_cost = fuel_cost + product_cost

            if total_cost < cheapest_cost and customer.money >= total_cost:
                cheapest_cost = total_cost
                best_shop = shop

        if best_shop:
            print(f"{customer.name}'s trip to {best_shop.name} "
                  f"costs {cheapest_cost:.2f}")
            customer.money -= cheapest_cost

            print(f"\nDate: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for item, quantity in customer.product_cart.items():
                cost = Decimal(shop.products[item]) * Decimal(quantity)
                print(f"{quantity} {item}s for {cost:.2f} dollars")
            print(f"Total cost is "
                  f"{customer.calculate_product_cost(best_shop):.2f} dollars")
            print("See you again!\n")
        else:
            print(f"{customer.name} doesn't have enough money to "
                  f"make a purchase in any shop")

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars\n")


if __name__ == "__main__":
    shop_trip()

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app import parsing

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
            customer_data["location"],
            customer_data["money"],
            customer_data["product_cart"],
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
        cheapest_cost = float("inf")

        for shop in shops:
            fuel_cost = customer.calculate_fuel_cost(customer.car, shop) * 2
            product_cost = customer.calculate_product_cost(shop)
            total_cost = round(fuel_cost + product_cost, 2)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost}")

            if total_cost < cheapest_cost and customer.money >= total_cost:
                cheapest_cost = total_cost
                best_shop = shop

        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}")

            print(f"\nDate: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            for item, quantity in customer.product_cart.items():
                cost = best_shop.products[item] * quantity
                if isinstance(cost, float) and cost.is_integer():
                    cost = int(cost)
                print(f"{quantity} {item}s for {round(cost, 2)} dollars")
            print(f"Total cost is "
                  f"{round(customer.calculate_product_cost(best_shop), 2)}"
                  f" dollars")
            print("See you again!\n")

            customer.money -= cheapest_cost

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()

import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app import parsing


def shop_trip() -> None:
    config = parsing.parse_data_from_json()
    customers_data = config["customers"]
    shops_data = config["shops"]

    for customer_data in customers_data:
        car_data = customer_data.get("car")
        if car_data:
            car = Car(car_data["brand"], car_data["fuel_consumption"])
        else:
            car = Car("Default Car", 10.0)

        customer = Customer(
            customer_data["name"],
            customer_data["location"],
            customer_data["money"],
            customer_data["product_cart"],
            car
        )

        fuel_cost = customer.calculate_fuel_cost(customer.car,
                                                 customer.location)
        customer.money -= fuel_cost
        shops = [Shop(shop_data["name"], shop_data["location"],
                      shop_data["products"]) for shop_data in shops_data]

        cheapest_cost = float("inf")
        best_shop = None

        for shop in shops:
            product_cost = customer.calculate_product_cost(shop)
            total_cost = round(fuel_cost + product_cost, 2)

            if total_cost < cheapest_cost and customer.money >= total_cost:
                cheapest_cost = total_cost
                best_shop = shop

        if best_shop:
            print(f"{customer.name}'s trip to the {best_shop.name}"
                  f" costs {total_cost}")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for item, quantity in customer.product_cart.items():
                cost = best_shop.products.get(item, 0) * quantity
                print(f"{quantity} {item}s for {round(cost, 2)} dollars")
            print(f"Total cost is {round(total_cost, 2)} dollars")
            print("See you again!")

            customer.money -= cheapest_cost

            print(f"{customer.name} rides to {best_shop.name}")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)}")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()

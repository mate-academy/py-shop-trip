import json
import datetime
from math import sqrt
from typing import List

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        information = json.load(file)

    def separate_data(
        data: dict,
        object_name: str
    ) -> list:
        """
        Separates data into different lists
        """
        separated_data = []
        for index in range(len(data.get(object_name))):
            separated_data.append(data.get(object_name)[index])
        return separated_data

    def create_customers() -> list:
        """
        Creates customers instances
        and returns list of customers
        """

        customers_data = separate_data(information, "customers")

        customers = []
        for customer in customers_data:
            customers.append(
                Customer(
                    name=customer["name"],
                    product_cart=dict(customer["product_cart"]),
                    initial_location=customer["location"],
                    car=Car(
                        brand=customer["car"]["brand"],
                        fuel_consumption=customer["car"]["fuel_consumption"]
                    ),
                    money=customer["money"]
                )
            )
        return customers

    def create_shops() -> list:
        """
        Creates shops instances
        and returns list of shops
        """

        shops_data = separate_data(information, "shops")

        shops = []
        for shop in shops_data:
            shops.append(
                Shop(
                    name=shop["name"],
                    location=shop["location"],
                    cost_of_products=dict(shop["products"]),
                )
            )
        return shops

    def calculate_fuel_expenses(
        car_fuel_consumption: float,
        customer_location: List[int],
        shop_location: List[int]
    ) -> float:
        """
        Calculates fuel expenses
        based on distance to the shop
        """
        fuel_price = information.get("FUEL_PRICE")
        # Calculate distance to the shop
        distance_to_shop = sqrt(
            (customer_location[0] - shop_location[0]) ** 2
            + (customer_location[1] - shop_location[1]) ** 2
        )
        # Calculate fuel amount needed
        fuel_needed = (
            car_fuel_consumption / 100
        ) * distance_to_shop
        # Calculate total fuel price
        return round(fuel_needed * fuel_price * 2, 2)

    def calculate_products_price(
        products_to_buy: dict,
        shop_products: dict
    ) -> dict:
        shopping_list = {"total_products_price": 0}
        for product, amount in products_to_buy.items():
            product_price = amount * shop_products[product]
            shopping_list["total_products_price"] += product_price
            shopping_list[product] = product_price
        return shopping_list

    def bought_products_list(
        customer: Customer
    ) -> None:
        for product, amount in customer.product_cart.items():
            print(
                f"{amount} {product}s for "
                f"{customer.products_bought[product]} dollars"
            )

    def print_receipt(
        customer: Customer
    ) -> None:
        total_cost = customer.products_bought.get("total_products_price")
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought: "
        )
        bought_products_list(customer)
        print(
            f"Total cost is {total_cost} dollars\n"
            "See you again!\n"
        )

    def calculate_trip_cost() -> None:
        customers = create_customers()
        shops = create_shops()

        shop_trip_cost = 100
        shop_to_ride = None

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            for shop in shops:
                products_price = calculate_products_price(
                    customer.product_cart,
                    shop.cost_of_products
                )
                current_shop_trip_cost = (
                    calculate_fuel_expenses(
                        customer.car.fuel_consumption,
                        customer.initial_location,
                        shop.location
                    ) + products_price.get("total_products_price")
                )
                print(
                    f"{customer.name}'s trip to the {shop.name} "
                    f"costs {current_shop_trip_cost}"
                )
                if current_shop_trip_cost < shop_trip_cost:
                    customer.products_bought = products_price
                    shop_trip_cost = current_shop_trip_cost
                    shop_to_ride = shop

            if customer.money > shop_trip_cost:
                customer.money = customer.money - shop_trip_cost
                print(
                    f"{customer.name} rides to {shop_to_ride.name}\n"
                )
                print_receipt(customer)
                print(
                    f"{customer.name} rides home\n"
                    f"{customer.name} now has {customer.money} dollars\n"
                )
            else:
                print(
                    f"{customer.name} doesn't have enough money"
                    f" to make a purchase in any shop"
                )

    calculate_trip_cost()


shop_trip()

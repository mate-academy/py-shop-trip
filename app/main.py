from app.customer import Customer
from app.shop import Shop
from app.car import Car
from app.utils import format_price
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    shops = []
    for shop_data in shops_data:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    customers = []
    for customer_data in customers_data:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"],
        )
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop, total_cost = customer.choose_shop(shops, fuel_price)

        if best_shop:
            distance = customer.calculate_distance(best_shop.location)
            print(f"{customer.name} rides to {best_shop.name}\n")
            fuel_cost = round(customer.car.get_fuel_cost
                              (distance * 2, fuel_price), 2)

            customer.location = best_shop.location
            best_shop.print_receipt(customer)

            product_total = 0
            for prod, amo in customer.product_cart.items():
                cost = round(best_shop.products[prod] * amo, 2)
                product_total += cost

            product_total = round(product_total, 2)
            total_spent = round(product_total + fuel_cost, 2)

            customer.money = round(customer.money - total_spent, 2)
            customer.location = customer.home

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{format_price(round(customer.money, 2))} dollars\n")
            customer.money = round(customer.money, 2)
        else:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")

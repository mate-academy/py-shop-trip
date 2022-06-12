import math
import datetime

from app.shop import Shop
from app.customer import Customer
from app.json_loader import get_fuel_price, get_shops, get_customers

FUEL_PRICE = get_fuel_price()
SHOPS = get_shops()
CUSTOMERS = get_customers()


def get_product_prices_in_some_shop(name: str) -> dict:
    if name in SHOPS:
        return SHOPS[name]["products"]


def create_shops() -> list[Shop]:
    shops = []
    for shop_data in SHOPS:
        shop = Shop(shop_data["name"],
                    shop_data["location"],
                    shop_data["products"])
        shops.append(shop)

    return shops


def create_customers() -> list[Customer]:
    customers = []
    for customer_data in CUSTOMERS:
        customer = Customer(customer_data["name"],
                            customer_data["product_cart"],
                            customer_data["location"],
                            customer_data["money"],
                            customer_data["car"])
        customers.append(customer)

    return customers


def distance_to_shop(home: list[int], shop: list[int]) -> float:
    return math.hypot(home[0] - shop[0], home[1] - shop[1])


def food_expenses(need_to_buy: dict, price: dict) -> (int, float):
    money_to_pay = 0

    for product in need_to_buy:
        if product in price:
            money_to_pay += need_to_buy[product] * price[product]

    return money_to_pay


def trip_price(customer: Customer, distance: float) -> float:
    return round(
        distance * 2 * (customer.car["fuel_consumption"] / 100 * FUEL_PRICE),
        2)


def shop_choices(customer: Customer) -> list[dict]:
    options = []

    for shop in SHOPS:
        option = {}
        food_price = food_expenses(customer.products, SHOPS[shop]["products"])
        distance = distance_to_shop(customer.location, SHOPS[shop]["location"])

        option["name"] = shop
        option["total_price"] = food_price + trip_price(customer, distance)
        options.append(option)

    return options


def best_choice(choices: list[dict]) -> dict:
    price = choices[0]["total_price"]
    for option in choices:
        if option["total_price"] < price:
            price = option["total_price"]

    for option in choices:
        for key, value in option.items():
            if value == price:
                return option


def shop_trip():
    customers = create_customers()
    result_dict_ = {}

    for customer in customers:
        result_dict_[customer] = shop_choices(customer)

    for customer, shops in result_dict_.items():
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            print(f"{customer.name}'s trip to the {shop['name']} "
                  f"costs {shop['total_price']}")

        best_shop = best_choice(shops)

        if customer.money < best_shop["total_price"]:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
            break
        else:
            print(f"{customer.name} rides to {best_shop['name']}\n")
            time_now = datetime.datetime.now()

            print(f"Date: {time_now.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")

            products_prices = get_product_prices_in_some_shop(
                best_shop["name"])
            for product_name, count in customer.products.items():
                cost = products_prices[product_name] * count
                print(f"{count} {product_name}s for {cost} dollars")

            total_cost = food_expenses(customer.products,
                                       SHOPS[best_shop["name"]]["products"])
            print(f"Total cost is {total_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.money -= best_shop["total_price"]
            print(f"{customer.name} now has {customer.money} dollars\n")


if __name__ == '__main__':
    shop_trip()

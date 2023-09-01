import json
# from datetime import datetime
import datetime
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def calculate_distance(location1, location2):
    return ((location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2) ** 0.5


def calculate_fuel_cost(distance, fuel_consumption, fuel_price):
    return (distance / 100) * fuel_consumption * fuel_price


def calculate_product_cost(product_cart, shop_products):
    return sum(product_cart[item] * shop_products.get(item, 0) for item in product_cart)


def format_money_decimals(cost):
    float_cost = float(round(cost, 2))
    return int(float_cost) if float_cost.is_integer() else float_cost


def format_datetime(dt):
    return dt.strftime('%d/%m/%Y %H:%M:%S')


def shop_trip():
    file_path = 'app/config.json'

    with open(file_path) as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
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
            customer_data["money"],
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
        print(f"{customer.name} has {format_money_decimals(customer.money)} dollars")
        min_total_cost = float('inf')
        best_shop = None

        for shop in shops:
            distance_to_shop = calculate_distance(customer.location, shop.location)
            fuel_cost_to_shop = calculate_fuel_cost(distance_to_shop, customer.car.fuel_consumption, fuel_price)

            total_product_cost = calculate_product_cost(customer.product_cart, shop.products)
            total_cost = 2 * fuel_cost_to_shop + total_product_cost

            print(f"{customer.name}'s trip to the {shop.name} costs {format_money_decimals(total_cost)}")

            if total_cost < min_total_cost and total_cost <= customer.money:
                min_total_cost = total_cost
                best_shop = shop

        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}\n")

            purchase_receipt = generate_purchase_receipt(customer, best_shop, fuel_cost_to_shop)
            print(purchase_receipt)

            print(f"{customer.name} rides home")

            remaining_money = customer.money - format_money_decimals(min_total_cost)
            print(f"{customer.name} now has {format_money_decimals(remaining_money)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


def generate_purchase_receipt(customer, shop, fuel_cost_to_shop):
    receipt = f"Date: {format_datetime(datetime.datetime.now())}\n"
    receipt += f"Thanks, {customer.name}, for your purchase!\nYou have bought: \n"
    total_purchase_cost = 0

    for item, quantity in customer.product_cart.items():
        if item in shop.products:
            item_cost = shop.products[item] * quantity
            receipt += f"{quantity} {item}s for {format_money_decimals(item_cost)} dollars\n"
            total_purchase_cost += item_cost
            # print(item, quantity, item_cost, total_purchase_cost)

    receipt += f"Total cost is {format_money_decimals(total_purchase_cost)} dollars\nSee you again!\n"
    return receipt

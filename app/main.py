from app.customer import Customer
from app.shop import Shop
from app.utils import is_integer
import datetime
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    customers_objects = []
    shops_objects = []
    fuel_price = data["FUEL_PRICE"]
    for customer in data["customers"]:
        customer_object = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        )
        customers_objects.append(customer_object)
    for shop in data["shops"]:
        shop_object = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shops_objects.append(shop_object)
    for customer in customers_objects:
        prices_of_trips = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_objects:
            shop_x = shop.location[0]
            shop_y = shop.location[1]
            customer_x = customer.location[0]
            customer_y = customer.location[1]
            fuel_consumption = customer.car["fuel_consumption"]
            first_part = (shop_x - customer_x) ** 2
            second_part = (shop_y - customer_y) ** 2
            distance = (first_part + second_part) ** 0.5
            fuel_cost = ((distance * 2) / 100) * fuel_consumption * fuel_price
            products_prices = {}
            for product, quantity in customer.products.items():
                price_of_product = shop.calculate_product_cost(
                    product, quantity)
                products_prices[product] = price_of_product
            sum_products_price = sum(products_prices.values())
            total_cost = sum_products_price + fuel_cost
            prices_of_trips[total_cost] = shop
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {round(total_cost, 2)}")
        smallest_price = min(prices_of_trips)
        if customer.money < smallest_price:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop")
            return
        target_index = shops_objects.index(prices_of_trips[smallest_price])
        target_store = shops_objects[target_index]
        print(f"{customer.name} rides to {target_store.name}\n")
        customer.location = target_store.location
        print(
            f"""Date: {datetime.datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S")}""")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        price_of_all_products = 0
        for product, quantity in customer.products.items():
            price_of_product = target_store.calculate_product_cost(
                product, quantity)
            price_of_product = is_integer(price_of_product)
            price_of_all_products += price_of_product
            print(f"{quantity} {product}s for {price_of_product} dollars")
        price_of_all_products = is_integer(price_of_all_products)
        print(f"Total cost is {price_of_all_products} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has "
            f"{round(customer.money - smallest_price, 2)} dollars\n")

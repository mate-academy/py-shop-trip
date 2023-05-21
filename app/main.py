import json
import datetime
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info_dict = json.load(file)
    customer_list = [
        Customer(
            customer.get("name"),
            customer.get("product_cart"),
            customer.get("location"),
            customer.get("money"),
            customer.get("car")
        )
        for customer in info_dict.get("customers")
    ]
    shop_list = [
        Shop(
            shop.get("name"),
            shop.get("location"),
            shop.get("products")
        )
        for shop in info_dict.get("shops")
    ]
    for customer in customer_list:
        cheapest_trip = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_list:
            cost_trip = (
                customer.total_cost_products_and_trip(
                    shop.products,
                    shop.location,
                    info_dict.get("FUEL_PRICE"))
            )
            cheapest_trip[cost_trip] = shop
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(cost_trip, 2)}")
        cheaper = min(cheapest_trip)
        chosen_shop = cheapest_trip.get(cheaper)
        if cheaper > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")

        else:
            print(f"{customer.name} rides to {chosen_shop.name}\n")
            print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            for product, quantity in customer.product_cart.items():
                cost_for_product = quantity * chosen_shop.products.get(product)
                print(f"{quantity} {product}s for {cost_for_product} dollars")
            print(f"Total cost is "
                  f"{customer.cost_of_products(chosen_shop.products)} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            money_after_shop = customer.money - cheaper
            print(f"{customer.name} now has "
                  f"{round(money_after_shop, 2)} dollars\n")

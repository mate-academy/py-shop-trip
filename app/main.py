import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    Car.fuel_price = data["FUEL_PRICE"]
    customers_list = []

    for customer in data["customers"]:
        customers_list.append(Customer(name=customer["name"],
                                       product_cart=customer["product_cart"],
                                       location=customer["location"],
                                       money=customer["money"],
                                       car=customer["car"]))

    shops_list = []
    for shop in data["shops"]:
        shops_list.append(Shop(name=shop["name"],
                               location=shop["location"],
                               products=shop["products"]))

    for customer in customers_list:
        product_cost = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_list:
            car_price = customer.car.trip_price(shop.location,
                                                customer.location)
            shop_price = shop.products_price(customer.product_cart)
            total_cost = round(shop_price + car_price, 2)
            product_cost[total_cost] = shop.name
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

        min_value = min(product_cost.keys())
        if customer.money >= min_value:
            cheapest_shop = Shop.shops[product_cost[min_value]]
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.buy_products(customer)
            customer.money -= min_value
            customer.car.to_home(name=customer.name, money=customer.money)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")


if __name__ == "__main__":
    shop_trip()

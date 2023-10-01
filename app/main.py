import json
from datetime import datetime

from car import Car
from customer import Customer
from shop import Shop


def calculate_distance(location1: list[int], location2: list[int]) -> float:
    x1, y1 = location1
    x2, y2 = location2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def shop_trip() -> None:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    fuel_price = config['FUEL_PRICE']
    customers_data = config['customers']
    shops_data = config['shops']

    customers = []
    shops = []

    for customer_data in customers_data:
        car_data = customer_data['car']
        car = Car(car_data['brand'], car_data['fuel_consumption'])
        customer = Customer(
            customer_data['name'],
            customer_data['product_cart'],
            customer_data['location'],
            customer_data['money'],
            car
        )
        customers.append(customer)

    for shop_data in shops_data:
        shop = Shop(
            shop_data['name'],
            shop_data['location'],
            shop_data['products']
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_trip = None
        min_trip_cost = float('inf')

        for shop in shops:
            distance_to_shop = calculate_distance(customer.location, shop.location)

            fuel_cost_to_shop = (distance_to_shop / 100) * customer.car.fuel_consumption * fuel_price

            product_cost = sum(
                customer.product_cart[product] * shop.products[product] for product in customer.product_cart)

            total_trip_cost = fuel_cost_to_shop + product_cost + fuel_cost_to_shop

            if total_trip_cost < min_trip_cost and total_trip_cost <= customer.money:
                min_trip_cost = total_trip_cost
                cheapest_trip = shop

        if cheapest_trip:
            print(f"{customer.name}'s trip to {cheapest_trip.name} costs {min_trip_cost:.2f}")
            customer.location = cheapest_trip.location

            current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print(f"\nDate: {current_time}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in customer.product_cart.items():
                product_price = cheapest_trip.products[product]
                product_total_cost = product_price * quantity
                print(f"{quantity} {product}s for {product_total_cost:.2f} dollars")
            print(f"Total cost is {min_trip_cost:.2f} dollars")
            print("See you again!\n")

            customer.money -= min_trip_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()

import datetime
import math
from app.customer import Customer
from app.shop import Shop


def cost_of_trip(customer: Customer,
                 shop: Shop,
                 fuel_price: float
                 ) -> float:
    distance = math.dist(customer.location, shop.location)
    cost_road = round(
        (customer.car.fuel_consumption / 100) * (distance * 2) * fuel_price, 2)
    cost_products = 0
    for product, quantity in customer.products.items():
        cost_products += shop.product_information.get(product, 0) * quantity
    return cost_road + cost_products


def define_shop(customer: Customer,
                shops: list[Shop],
                fuel_price: float
                ) -> int:
    result = []
    for shop in shops:
        trip_costs = cost_of_trip(customer, shop, fuel_price)
        result.append(trip_costs)
        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {trip_costs}")
    return result.index(min(result))


def receipt(shop: Shop, customer: Customer) -> None:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought: ")
    total_cost = 0
    for product, count in customer.products.items():
        total_cost += count * shop.product_information.get(product, 0)
        print(f"{count} {product if count < 2 else product + 's'} "
              f"for "
              f"{count * shop.product_information.get(product, 0)} dollars")
    print(f"Total cost is {round(total_cost, 2)} dollars")
    print("See you again!")


def go_to_shop(customer: Customer, shop: Shop, fuel_price: float) -> None:
    trip_price = cost_of_trip(customer, shop, fuel_price)
    customer.money -= trip_price
    print(f"{customer.name} rides to {shop.name}\n")
    receipt(shop, customer)
    print(f"\n{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars\n")


def can_afford_trip(customer: Customer,
                    shops: list[Shop],
                    fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop = define_shop(customer, shops, fuel_price)
    trip_cost = cost_of_trip(customer, shops[cheapest_shop], fuel_price)
    if trip_cost < customer.money:
        go_to_shop(customer, shops[cheapest_shop], fuel_price)
    else:
        print(f"{customer.name} "
              "doesn't have enough money to make a purchase in any shop")

import datetime
from math import dist
from app.shop import Shop
from app.customer import Customer


def receipt(shop: Shop, customer: Customer) -> None:
    current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {current_date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    total_cost = 0
    for product, count in customer.wanted_products.items():
        price = shop.provided_products.get(product, 0)
        total_cost += count * price
        print(
            f"{count} {product if count < 2 else product + 's'} "
            f"for {count * price} dollars"
        )
    print(f"Total cost is {round(total_cost, 2)} dollars")
    print("See you again!")


def choose_shop(customer: Customer,
                shops: list[Shop],
                fuel_price: float) -> int:
    trip_costs = []
    for shop in shops:
        trip = trip_cost(customer, fuel_price, shop)
        trip_costs.append(trip)
        print(f"{customer.name}'s trip to "
              f"{shop.name} " f"costs {trip_cost}")
    return trip_costs.index(min(trip_costs))


def trip_cost(customer: Customer, fuel_price: float, shop: Shop) -> float:
    distance = dist(customer.location, shop.location)
    fuel_consumption = customer.car.fuel_consumption
    if fuel_consumption is not None:
        fuel_cost = round((fuel_consumption / 100) * (distance * 2) * fuel_price, 2)
        return fuel_cost
    else:
        return 0.0


def go_shop(customer: Customer,
            shop: Shop,
            fuel_price: float) -> None:
    trip_price = trip_cost(customer, fuel_price, shop)
    customer.money -= trip_price
    print(f"{customer.name} rides to {shop.name}\n")
    receipt(shop, customer)
    print(f"\n{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars\n")


def can_afford_trip(customer: Customer,
                    shops: list[Shop],
                    fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop_index = choose_shop(customer, shops, fuel_price)
    trip = trip_cost(customer, fuel_price, shops[cheapest_shop_index])
    if trip < customer.money:
        go_shop(customer, shops[cheapest_shop_index], fuel_price)
    else:
        print(f"{customer.name} doesn't have money")

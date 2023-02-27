from app.instances.customer import Customer
from app.instances.shop import Shop


def find_distance_to_shop(
        customer_location: list,
        shop_location: list
) -> int | float:
    return (
        (customer_location[0] - shop_location[0]) ** 2
        + (customer_location[1] - shop_location[1]) ** 2
    ) ** 0.5


def calculate_fuel_cost_one_way(
        fuel_price: int | float,
        car_fuel_consumption: int | float,
        distance: int | float
) -> int | float:
    return fuel_price * car_fuel_consumption / 100 * distance


def calculate_product_cart_cost(
        products_to_buy: dict,
        products_costs: dict
) -> int | float:
    total_cost = 0
    for product_name, quantity in products_to_buy.items():
        if product_name in products_costs:
            total_cost += products_costs.get(product_name) * quantity
    return total_cost


def calculate_trips_costs_to_shops(
        fuel_price: int | float,
        customer: Customer,
        shops: list
) -> dict:
    print(f"{customer.name} has {customer.money} dollars")

    shop_and_trip_cost = {}

    for shop in shops:
        distance = find_distance_to_shop(customer.home_location, shop.location)
        fuel_by_distance_cost = calculate_fuel_cost_one_way(
            fuel_price,
            customer.car_fuel_consumption,
            distance
        )
        product_cart_cost = calculate_product_cart_cost(
            customer.product_cart,
            shop.products
        )
        trip_cost = round(fuel_by_distance_cost * 2 + product_cart_cost, 2)
        shop_and_trip_cost[shop] = trip_cost

        print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")

    return shop_and_trip_cost


def check_if_can_ride_to_shop(
        customer: Customer,
        trips_to_shops_costs: dict
) -> None:
    cheapest_trip_cost = min(trips_to_shops_costs.values())

    if customer.money >= cheapest_trip_cost:
        for shop_instance, trip_cost in trips_to_shops_costs.items():
            if cheapest_trip_cost == trip_cost:
                customer.has_enough_money = True
                customer.chosen_shop = shop_instance
                customer.money -= cheapest_trip_cost
    else:
        print(f"{customer.name} doesn't have "
              f"enough money to make purchase in any shop")


def ride_to_shop(customer: Customer, shop: Shop) -> None:
    print(f"{customer.name} rides to {shop.name}\n")
    customer.current_location = shop.location


def ride_home(customer: Customer) -> None:
    print(f"{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars\n")
    customer.current_location = customer.home_location
    customer.has_enough_money = False
    customer.chosen_shop = None

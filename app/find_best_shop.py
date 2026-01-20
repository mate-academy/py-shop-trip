from app.car import Car
from app.customer import Customer
from app.info_dict import InfoDict


def find_the_best_shop(
        customer: Customer,
        info_dict: InfoDict,
        car: Car
) -> dict:

    best_option_shop = {}

    for shop in info_dict.shops:
        distance = customer.get_distance(shop)
        cost = car.cost_of_travel(distance, info_dict.fuel_price)
        total_cost = round(
            (shop.calculate_products_price(customer.product_cart)
             + cost), 2
        )

        if total_cost <= customer.money:
            best_option_shop[total_cost] = shop

        print(f"{customer.name}'s trip to "
              f"the {shop.name} costs {total_cost}")

    return best_option_shop

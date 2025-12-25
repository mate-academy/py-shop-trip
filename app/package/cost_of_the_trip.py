from math import sqrt

from app.customer import Customer
from app.shop import Shop


def get_distance_cost(customer: Customer,
                      shops: list[Shop],
                      car: dict,
                      fuel_price: float,
                      store_prices: list) -> tuple[float, int]:
    """
    distances -> get the distance to each store;
    fuel_cost -> calculate the cost of fuel in both directions;
    total_cost -> get the total costs (road + purchases in the shop);
    shop_ind -> get the index of the store we need.
    """
    distances = distance_to_shop(customer, shops)

    fuel_cost = [
        round(distance * 2 * (car["fuel_consumption"]) / 100 * fuel_price, 2)
        for distance in distances
    ]

    total_cost = [fuel_cost[i] + store_prices[i][3]
                  for i in range(len(fuel_cost))]

    for i, shop in zip(range(3), shops):
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {total_cost[i]}")

    shop_ind = total_cost.index(min(total_cost))
    if min(total_cost) < customer.money:
        print(f"{customer.name} rides to {shops[shop_ind].name}\n")
    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")

    return min(total_cost), shop_ind


def distance_to_shop(customer: Customer, shops: list[Shop]) -> list[float]:
    """
    We calculate the distance between the customer and each shop.
    """
    distances = []
    for shop in shops:
        distance_x = customer.location[0] - shop.location[0]
        distance_y = customer.location[1] - shop.location[1]
        distances.append(sqrt(distance_x ** 2 + distance_y ** 2))

    return distances

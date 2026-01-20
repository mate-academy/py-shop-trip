import math
from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer
    from app.shop import Shop


def get_distance(num_a: list, num_b: list) -> float:
    return math.sqrt((num_b[0] - num_a[0]) ** 2 + (num_b[1] - num_a[1]) ** 2)


def choose_cheapest_shop(
        customer: "Customer",
        shops: list["Shop"],
        fuel_price: float
) -> tuple[Any, Any]:

    costs = {}
    print(f"{customer.name} has {customer.money} dollars")
    for shop in shops:
        cost = customer.full_trip_cost(shop, fuel_price)
        print(f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}")
        costs[shop] = cost
    cheapest_shop = min(costs, key=costs.get)
    return cheapest_shop, costs[cheapest_shop]

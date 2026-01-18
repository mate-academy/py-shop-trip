from typing import List
from app.customer import Customer


def best_price_shop(customers: List[Customer]) -> None:
    for customer in customers:
        cheapest_shop = min(customer.total_trip_cost,
                            key=customer.total_trip_cost.get)
        cheapest_cost = customer.total_trip_cost[cheapest_shop]

        customer.cheapest_shop = cheapest_shop
        customer.cheapest_cost = cheapest_cost

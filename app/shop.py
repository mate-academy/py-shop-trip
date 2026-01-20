import math
import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products


def shopping(
        name: str,
        products: dict,
        prices: dict
) -> None:
    print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
    print(f"Thanks, {name}, for your purchase!")
    print("You have bought:")
    total_cost = 0
    for product in products:
        total_sum_for_product = prices[product] * products[product]
        if total_sum_for_product == int(total_sum_for_product):
            total_sum_for_product = int(total_sum_for_product)
        print(
            f"{products[product]} {product}s "
            f"for {total_sum_for_product} dollars"
        )
        total_cost += total_sum_for_product

    print(
        f"Total cost is {total_cost} dollars\n"
        f"See you again!\n"
    )


def find_trip_cost(
        customer_location: list,
        shop_location: list,
        fuel_price: int | float,
        fuel_consumption: int | float
) -> float | int:
    distance = math.dist(customer_location, shop_location)
    trip_cost = (distance * 2 * fuel_consumption * fuel_price) / 100
    return round(trip_cost, 2)

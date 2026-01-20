from datetime import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def create_instances(customers: dict, shops: dict) -> tuple[
    list[Customer],
    list[Shop]
]:
    return (
        [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            ) for customer in customers
        ],
        [
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            ) for shop in shops
        ]
    )


def calculate_distance_to_shop(
        customer_loc: list[int],
        shop_loc: list[int]
) -> float:
    x_axis = (shop_loc[0] - customer_loc[0]) ** 2
    y_axis = (shop_loc[1] - customer_loc[1]) ** 2
    return (x_axis + y_axis) ** 0.5


def shop_receipt(
        customers_cart: dict,
        shop_price: dict
) -> float:
    return sum(
        [
            customers_cart[key] * shop_price[key]
            for key in customers_cart
        ]
    )


def total_trip_cost(
        fuel_price: float,
        customers: list[Customer],
        shops: list[Shop]
) -> None:
    for customer in customers:
        for shop in shops:
            distance = calculate_distance_to_shop(
                customer.location,
                shop.location
            )
            receipt_cost = shop_receipt(
                customer.products_cart,
                shop.products
            )
            total_price = round(
                receipt_cost
                + (distance * 2 * customer.car.fuel_consumption / 100)
                * fuel_price, 2
            )
            customer.trips_costs[f"{shop.name}"] = total_price


def customer_can_go_to_shop(customer: Customer) -> str | None:
    print(f"{customer.name} has {customer.money} dollars")
    for shop in customer.trips_costs:
        print(f"{customer.name}'s trip to the {shop} "
              f"costs {customer.trips_costs[shop]}")
    customers_minimal_trip_cost = min(customer.trips_costs.values())
    if customers_minimal_trip_cost <= customer.money:
        shop_name = list(customer.trips_costs.keys())[
            list(customer.trips_costs.values()).index(
                min(customer.trips_costs.values()))]
        print(f"{customer.name} rides to {shop_name}\n")
        return shop_name
    print(f"{customer.name} doesn't have enough money "
          f"to make a purchase in any shop")


def print_shop_receipt(
        customer: Customer,
        shops: list[Shop],
        shop_name: str
) -> None:
    product_names = [product for product in customer.products_cart]
    for shop in shops:
        if shop.name == shop_name:
            date = datetime(2021, 1, 4, 12, 33, 41)
            receipt_lines = [f'Date: {date.strftime("%d/%m/%Y %H:%M:%S")}\n',
                             f"Thanks, {customer.name}, "
                             f"for your purchase!\n",
                             "You have bought:\n"]
            for product in product_names:
                quantity = customer.products_cart.get(product, 0)
                price = shop.products.get(product, 0)
                total = quantity * price
                total = int(total) if total % 1 == 0 else total
                receipt_lines.append(
                    f"{quantity} {product}s for {total} dollars\n"
                )
            total_cost = shop_receipt(customer.products_cart, shop.products)
            receipt_lines.append(
                f"Total cost is {total_cost} dollars\n"
            )
            receipt_lines.append("See you again!\n")
            print("".join(receipt_lines))


def taking_back_home(customer: Customer, total_price: float) -> None:
    customer.money -= total_price
    print(f"{customer.name} rides home\n"
          f"{customer.name} now has {round(customer.money, 2)} dollars\n")

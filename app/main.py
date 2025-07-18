import json

from app.customer import Customer
from app.shop import Shop


def choose_shop(
    customer: Customer,
    shops: list[Shop],
    fuel_price: float
) -> tuple[Shop, float]:
    min_cost = float("inf")
    best_shop: Shop | None = None

    for shop in shops:
        distance = customer.location.distance(shop.location)
        cost = (
            2 * customer.car.calculate_cost(distance, fuel_price)
            + shop.calculate_cost(customer.product_cart)[0]
        )
        print(
            f"{customer.name}'s trip to "
            f"the {shop.name} costs {round(cost, 2)}"
        )

        if min_cost > cost:
            min_cost = cost
            best_shop = shop

    return best_shop, min_cost


def shop_trip(filename: str = "app/config.json") -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    fuel_price: float = data.get("FUEL_PRICE")
    customers: list[Customer] = [
        Customer.from_dict(customer)
        for customer in data.get("customers", [])
    ]
    shops: list[Shop] = [
        Shop.from_dict(shop)
        for shop in data.get("shops", [])
    ]

    for customer in customers:
        print(f"{customer.name} has {round(customer.money, 2)} dollars")
        shop, cost = choose_shop(customer, shops, fuel_price)
        if cost > customer.money:
            print(
                f"{customer.name} doesn't have "
                "enough money to make a purchase in any shop"
            )
            continue
        print(f"{customer.name} rides to {shop.name}")

        shop.print_purchase(customer)
        customer.money -= cost

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {round(customer.money, 2)} dollars")

        print()

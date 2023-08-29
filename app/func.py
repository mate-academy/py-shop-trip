from app.customer import Customer
from app.shop import Shop


def distance(point1: list[int], point2: list[int]) -> float:
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def shopping(customer: Customer,
             cheapest_shop: Shop,
             other_shops: dict) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    for cost, shop in other_shops.items():
        print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
    if customer.money >= customer.needed_money:
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        home_location = customer.location
        customer.location = cheapest_shop.location

        cheapest_shop.print_receipt(customer)

        print(f"{customer.name} rides home")
        customer.location = home_location

        customer.money -= customer.needed_money
        print(f"{customer.name} now has {customer.money} dollars\n")

    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")

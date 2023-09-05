from app.shop import Shop
from app.customer import Customer


def fuel_price(
    shop: Shop,
    customer: Customer,
    liter_price: float
) -> float:
    x_point = (customer.location[0] - shop.location[0]) ** 2
    y_point = (customer.location[1] - shop.location[1]) ** 2
    distance = (x_point + y_point) ** 0.5

    price = distance * customer.car["fuel_consumption"] / 100 * liter_price * 2
    return price


def drive_to_shop(
        shop: Shop,
        customer: Customer
) -> None:
    print(f"{customer.name} rides to {shop.name}\n")
    customer.location = shop.location


def drive_to_home(
        customer: Customer
) -> None:
    print(f"{customer.name} rides home")
    customer.location = customer.home_location

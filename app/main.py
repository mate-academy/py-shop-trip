import math

from app.handle_config import handle_config
from app.shop import Shop
from app.customer import Customer


def count_road_price(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float:
    x1, y1 = customer.location
    x2, y2 = shop.location
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    fuel_spent = distance * (customer.car.fuel_consumption / 100)
    return round(fuel_spent * fuel_price * 2, 2)


def count_trip_price(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> tuple:
    road_price = count_road_price(customer, shop, fuel_price)

    products_price = 0
    for product, amount in customer.product_cart.items():
        products_price += shop.products[product] * amount

    price = road_price + products_price
    print(f"{customer.name}'s trip to the {shop.name} costs {price}")
    return price, shop


def choose_shop(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> tuple:
    min_cost = []

    for shop in shops:
        min_cost.append(count_trip_price(customer, shop, fuel_price))

    return min(min_cost)


def drive_to_shop(customer: Customer, shop: Shop, price: int) -> None:
    print(f"{customer.name} rides to {shop.name}\n")
    home = customer.location
    customer.location = shop.location
    customer.money -= price
    shop.buy_products(customer)
    customer.location = home


def shop_trip() -> None:
    fuel_price, customers, shops = handle_config()
    for customer in customers:
        customer.count_money()
        price, shop = choose_shop(customer, shops, fuel_price)
        if customer.money >= price:
            drive_to_shop(customer, shop, price)
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()

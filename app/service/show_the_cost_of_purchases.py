from app.classes.customer import Customer
from app.classes.shop import Shop


def show_the_cost_of_purchases(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> None:
    prices = {}
    for shop in shops:
        total_price = customer.calculate_cost_shopping(shop, fuel_price)
        print(f"{customer.name}'s trip to the {shop.name} costs {total_price}")
        prices[shop.name] = total_price
    min_price = min(prices.values())
    if min_price > customer.money:
        print(f"{customer.name} doesn't have enough money"
              f" to make a purchase in any shop")
        customer.is_enough_money = False
        return
    customer.is_enough_money = True
    shop_name = None
    for name, price in prices.items():
        if price == min_price:
            shop_name = name
            break
    customer.shop = shop_name
    print(f"{customer.name} rides to {shop_name}\n")

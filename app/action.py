from typing import Any

from app.distance import Distance
from app.shop import Shop


def list_to_buy(
        product: str,
        quantity: int,
        price: float | int
) -> None:
    print(f"{quantity} {product}s for {price * quantity} dollars")


def total_cost_products(
        customer: Any,
        shop: Shop
) -> int | float:
    total_price = 0
    for product, price in shop.products.items():
        if product in customer.products:
            total_price += price * customer.products[product]
    return total_price


def min_price(
        customer: Any,
        shops: [Shop],
        distance: Distance,
        full_price: int | float
) -> float | int:
    shop_prices = {}
    for shop in shops:
        cost = total_cost(customer, shop, distance, full_price)
        if shop.name not in shop_prices:
            shop_prices[shop.name] = cost
    name_shop = min(shop_prices, key=shop_prices.get)
    return name_shop


def total_cost(
        customer: Any,
        shop: Shop,
        distance: Distance,
        full_price: int | float
) -> int | float:
    fuels_price = distance.fuel_price(
        customer.location, shop.location, full_price, customer.car
    )
    cost = total_cost_products(customer, shop) + fuels_price
    return cost

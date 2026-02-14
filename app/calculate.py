from decimal import Decimal
from math import sqrt

from app.customer import Customer
from app.shop import Shop


def calculate_products(customer: Customer, shop: Shop) -> Decimal | None:
    price = Decimal("0")
    for key, value in customer.product_cart.items():
        shop_price = shop.products.get(key)
        if shop_price is not None:
            price += Decimal(str(shop_price)) * Decimal(str(value))
        else:
            return Decimal("Infinity")
    return price.quantize(Decimal("0.01"))


def calculate_distance(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> Decimal:
    fuel_price = Decimal(str(fuel_price))
    distance = sqrt(
        (customer.location[0] - shop.location[0]) ** 2
        + (customer.location[1] - shop.location[1]) ** 2
    )
    result = (Decimal(str(distance))
              * Decimal("2")
              * fuel_price
              * Decimal(str(customer.car.fuel_consumption)) / Decimal("100")
              )
    return result.quantize(Decimal("0.01"))

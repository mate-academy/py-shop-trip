from app.customer import Customer
from app.shop import Shop


def trip_and_shop_price(shop: Shop, customer: Customer,
                        fuel_price: float | int) -> float | int:
    product_price = shop.calculate_price(customer.product_cart)
    fuel_cost = customer.car.trip_price(
        customer.distance(shop.location), fuel_price)
    return round(product_price + fuel_cost * 2, 2)

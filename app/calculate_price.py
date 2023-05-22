from app.customer import Customer
from app.shop import Shop


def calculate_distance(customer_location: list, shop_location: list) -> float:
    return ((customer_location[0] - shop_location[0]) ** 2 + (
            customer_location[1] - shop_location[1]) ** 2) ** 0.5


def calculate_trip_price(customer: Customer, shop: Shop,
                         fuel_price: float) -> float:
    # full distance: from home to shop and back
    dist = calculate_distance(customer.location, shop.location) * 2
    dist_price = customer.car.fuel_consumption / 100 * dist * fuel_price

    products_price = sum(shop.products[product] * amount for product, amount in
                         customer.product_cart.items())

    return dist_price + products_price

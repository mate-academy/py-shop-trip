from app.customer import Customer
from app.shop import Shop


def calculate_trip_cost(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float:
    distance = (abs(customer.location[0] - shop.location[0])
                ** 2 + abs(customer.location[1] - shop.location[1])
                ** 2) ** 0.5
    cost = ((distance * 2 * customer.car_consumption / 100 * fuel_price)
            + customer.milk * shop.price_milk
            + customer.butter * shop.price_butter
            + customer.bread * shop.price_bread)
    return round(cost, 2)

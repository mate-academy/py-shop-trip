import math


def trip_cost_calculation(
        customer_location: list,
        shop_location: list,
        car_fuel_consumption: float,
        customer_product_cart: dict,
        shop_products: dict,
        fuel_price: float,
) -> tuple:
    distance = math.sqrt((customer_location[0] - shop_location[0])**2
                         + (customer_location[1] - shop_location[1]) ** 2)

    amount_of_fuel_consumption = (
        fuel_price * ((car_fuel_consumption / 100) * distance)
    )

    total_amount_for_products = (
        sum(value1 * value2 for (value1, value2) in
            zip(customer_product_cart.values(), shop_products.values())))
    total_price = total_amount_for_products + amount_of_fuel_consumption * 2

    return round(total_price, 2), round(total_amount_for_products, 2)

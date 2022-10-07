def fuel_calculation(
        fuel_price: float,
        fuel_consumption: float,
        shop_location: list,
        customer_location: list) -> float:
    x_coord = shop_location[0] - customer_location[0]
    y_coord = shop_location[1] - customer_location[1]
    distance = (x_coord * x_coord + y_coord * y_coord) ** 0.5
    result = distance * fuel_consumption / 100 * fuel_price
    return result

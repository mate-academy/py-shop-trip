def trip_cost(customer: object, shop: object) -> int | float:
    x1, y1 = customer.location
    x2, y2 = shop.location
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    consumptions_per_km = customer.car["fuel_consumption"] / 100
    cost = (distance * consumptions_per_km) * customer.fuel_price

    return round(cost * 2, 2)

from app.customer import dane


def fuel_price() -> float:
    return dane["FUEL_PRICE"]


def prize_for_fuel(distance: float, fuel_consumption: float) -> float:
    return (distance * fuel_consumption * fuel_price()) / 100

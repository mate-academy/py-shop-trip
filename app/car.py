from app.config_loader import load_config

config = load_config()


class Car:
    FUEL_PRICE: int = config["FUEL_PRICE"]

    def __init__(self, car_params: dict) -> None:
        self.brand = car_params.get("brand")
        self.fuel_consumption = car_params.get("fuel_consumption")

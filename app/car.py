class Car:
    def __init__(self, info: dict) -> None:
        self.brand = info.get("brand", "Unknown")
        self.fuel_consumption = info.get("fuel_consumption", 0)

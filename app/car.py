class Car:
    def __init__(self, name: str, volume: float) -> None:
        self.name = name
        self.volume = volume

    def price_for_km(self, fuel_price: float) -> float:
        return round(self.volume * fuel_price / 100, 2)

from app.calculator import ShopTripCalculator


def shop_trip() -> None:
    trip_calculator = ShopTripCalculator("app/config.json")
    trip_calculator.run()


shop_trip()

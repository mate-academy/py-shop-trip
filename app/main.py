from app.calculator import ShopTripCalculator


def shop_trip() -> None:
    trip_calculator = ShopTripCalculator("app/config.json")
    trip_calculator.run()


if __name__ == "__main__":
    shop_trip()

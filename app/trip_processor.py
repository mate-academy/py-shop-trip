from app.deserializer import Deserializer


class TripProcessor:
    def __init__(self) -> None:
        self.data = Deserializer()

    def process_users(self) -> None:
        for customer in self.data.customers:
            customer.print_info()
            customer.calculate_all_shops_trip(
                self.data.shops,
                self.data.fuel_price
            )
            customer.shop_trip()

from app.data_manager import DataManager


def shop_trip() -> None:
    data_manager = DataManager()
    customers = data_manager.create_customers()
    shops = data_manager.create_shops()

    for customer in customers:
        customer.calc_minimal_cost_trip_to_shops(shops)


shop_trip()

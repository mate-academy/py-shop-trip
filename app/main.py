from app.Info import Info
from app.Customers import ShopTrip
from app.Shops import Shop


def shop_trip() -> None:
    info = Info()
    for name_customer in info.names_customers():

        shop_trips = ShopTrip(name_customer)
        purchase_in_shop = Shop(name_customer)

        # Check how much money have customer
        shop_trips.customers_money()
        # Calculate low-priced variant
        shop_trips.calculate_cost_trip()
        # Check if we have enough money
        if shop_trips.ride_to_the_shop() is False:
            continue
        # Change location customer
        purchase_in_shop.change_location()
        # Print receipt
        purchase_in_shop.receipt()
        # Go home and count money
        purchase_in_shop.ride_home()


shop_trip()

from app.Info import Info
from app.Customers import ShopTrip
from app.Shops import Shop


def shop_trip() -> None:
    info = Info()
    for name_customer in info.names_customers():
        shop_trips = ShopTrip(name_customer)
        purchase_in_shop = Shop(name_customer)
        shop_trips.customers_money()
        shop_trips.calculate_cost_trip()
        if shop_trips.ride_to_the_shop() is False:
            continue
        purchase_in_shop.change_location()
        purchase_in_shop.receipt()
        purchase_in_shop.ride_home()


shop_trip()

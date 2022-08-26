from app.shop_trip import ShopTrip


def shop_trip():
    trip = ShopTrip("app/config.json")
    trip.all_customers_trip()

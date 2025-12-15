from app.customer import Customer
from app.data_loader import loader
from app.shop import Shop
from app.shop_trip_manager import ShopTripManager


def shop_trip() -> None:
    fuel_price_dict, customers_dict, shops_dict = loader("app/config.json")

    manager = ShopTripManager(fuel_price_dict)

    customers = [Customer.from_dict(customer) for customer in customers_dict]
    shops = [Shop.from_dict(shop) for shop in shops_dict]

    for customer in customers:
        cheapest_shop = manager.get_cheapest_shop_trip(customer, shops)
        if cheapest_shop:
            manager.move_to(customer, cheapest_shop)
            print("")
            manager.do_shopping(customer, cheapest_shop)
            print("")
            manager.move_home(customer)
            print(f"{customer.name} "
                  f"now has {round(customer.money, 2)} dollars")
            print("")


shop_trip()

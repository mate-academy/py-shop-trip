from app.config_loader import load_config
from app.customer import Customer
from app.shop import Shop


config = load_config()
customers = [Customer(customer) for customer in config.get("customers")]
shops = [Shop(shop) for shop in config.get("shops")]


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop = customer.choose_nearest_shop(shops)
        trip_cost = customer.trip_cost(shop)

        if trip_cost > customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {shop.name}\n")

            customer.location = shop.location
            customer.buy_products_in_shop(shop)
            customer.money -= trip_cost

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")

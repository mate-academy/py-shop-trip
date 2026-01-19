from app.data_processing.calculations import (
    homecoming,
    shop_offer,
    attending_shop)
from app.data_processing.data_initialization import (
    create_account,
    create_shop,
    get_data)
from app.structures.customer_profile import Car


def shop_trip() -> None:
    filename = "app/config.json"
    data = get_data(filename)
    for client in data.get("customers"):
        customer = create_account(client)
        customer.wallet()
        Car.set_fuel_price(data.get("FUEL_PRICE"))

        offers = []
        for shop in data.get("shops"):
            shop = create_shop(shop)
            shop, cost = shop_offer(customer, shop)
            offers.append([shop, cost])
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")

        choice = min(offers, key=lambda item: item[1])
        prefer_shop, cost_groceries = choice
        if cost_groceries <= customer.money:
            attending_shop(customer, prefer_shop)
            print()
            homecoming(customer, prefer_shop)
            print()
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()

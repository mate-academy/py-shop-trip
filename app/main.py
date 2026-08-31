from app.initialisation import initialisation


def shop_trip() -> None:
    fuel_price, customers, shops = initialisation("config.json")

    for customer in customers:
        best_shop, best_price = customer.choose_shop(shops, fuel_price)

        if customer.enough_money(best_price):
            customer.buy(best_shop, best_price)
        else:
            customer.not_enough_money()


if __name__ == "__main__":
    shop_trip()

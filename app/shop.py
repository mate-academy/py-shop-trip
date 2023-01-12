from datetime import datetime as dt


class Shop:
    shops = []

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops.append(self)

    @staticmethod
    def store_cashier(
            name: str,
            store: str,
            products: dict,
            money: float
    ) -> None:

        basket = None
        for shop in Shop.shops:
            if shop.name == store:
                basket = shop
        print(f"\nDate: "
              f"{dt(2021, 4, 1, 12, 33, 41).strftime('%m/%d/%Y %H:%M:%S')}\n"
              f"Thanks, {name}, for you purchase!"
              f"\nYou have bought: ")
        total = 0

        for key, value in basket.products.items():
            total += products[key] * value
            print(f"{products[key]} {key}s for "
                  f"{products[key] * value} dollars")
        print(f"Total cost is {total} dollars\n"
              f"See you again!\n"
              f"\n{name} rides home\n"
              f"{name} now has {round(money - total, 2)} dollars\n")

import datetime as dt


class Shop:
    shops = {}

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops.update({self.name: self})

    def store_cashier(
            self,
            name: str,
            products: dict,
            money: float
    ) -> None:

        basket = self.products
        print(f"\nDate: "
              f"{dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {name}, for you purchase!"
              f"\nYou have bought: ")
        total = 0

        for product, count in basket.items():
            total += products[product] * count
            print(f"{products[product]} {product}s for "
                  f"{products[product] * count} dollars")
        print(f"Total cost is {total} dollars\n"
              f"See you again!\n"
              f"\n{name} rides home\n"
              f"{name} now has {round(money - total, 2)} dollars\n")

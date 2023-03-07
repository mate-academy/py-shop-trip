import datetime

from app.client_resources.Point2D import Point2d


class Shop:
    def __init__(self, name: str,
                 location: Point2d,
                 products: dict[str, int]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def sell_products(self,
                      person: object,
                      products: dict[str]) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {person.name}, for your purchase!")
        print("You have bought: ")

        total_price = 0
        for name, count in products.items():
            total_price += self.products[name] * count
            self.sell_product(person, name, count)

        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")

    def sell_product(self,
                     person: object,
                     product: str,
                     count: int) -> None:
        person.money -= self.products[product] * count
        print(f"{count} {product}s for "
              f"{self.products[product] * count} dollars")

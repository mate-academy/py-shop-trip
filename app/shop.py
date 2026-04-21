from __future__ import annotations


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return f"Shop(name={self.name})"

    def __repr__(self) -> str:
        return self.__str__()

    def total_price(self, products: dict) -> float:
        result = 0
        for product, count in products.items():
            result += count * self.products[product]
        return result

    def print_check(self, name: str, products: dict) -> None:
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        for product, count in products.items():
            price = self.products[product] * count
            print(f"{count} {product}s for "
                  f"{int(price) if int(price) == price else price} dollars")
        print(f"Total cost is {self.total_price(products)} dollars")
        print("See you again!")

    @classmethod
    def make_shops(cls, shops: list) -> list:
        return [
            cls.from_dict(shop)
            for shop in shops
        ]

    @classmethod
    def from_dict(cls, item: dict) -> Shop:
        return cls(
            name=item["name"],
            location=item["location"],
            products=item["products"]
        )

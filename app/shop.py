from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def total_price(self, product_cart: dict) -> float:
        return round(
            sum(
                self.products[product] * price_product
                for product, price_product in product_cart.items()
            )
            , 2
        )

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def list_constructor(cls, shops_list: list) -> list:
        for index, shop in enumerate(shops_list):
            shops_list[index] = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )

        return shops_list

    def buy_product(self, product_cart: dict) -> None:
        total_price = 0

        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            total_price += price

            print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is {total_price} dollars\nSee you again!\n")

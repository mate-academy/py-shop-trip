import json

from app.customer import Customer


class Shop:
    shops = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def add_to_shops(cls) -> None:
        with open("app/config.json", "r") as shop_file:
            shop_data = json.load(shop_file)
            for shop in shop_data["shops"]:
                shop = cls(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"],
                )
                cls.shops.append(shop)

    @staticmethod
    def buy_product(customer: Customer, name_shop: str) -> None:
        for shop in Shop.shops:
            if shop.name == name_shop:
                cost_milk = customer.product_cart["milk"] \
                    * shop.products["milk"]
                cost_bread = customer.product_cart["bread"] \
                    * shop.products["bread"]
                cost_butter = customer.product_cart["butter"] \
                    * shop.products["butter"]
                print(f"{customer.product_cart['milk']} milks for "
                      f"{cost_milk} dollars\n"
                      f"{customer.product_cart['bread']} breads for "
                      f"{cost_bread} dollars\n"
                      f"{customer.product_cart['butter']} butters for "
                      f"{cost_butter} dollars")

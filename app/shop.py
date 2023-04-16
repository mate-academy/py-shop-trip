from app.convert_from_json import shop_list


class Shop:
    def __init__(
            self,
            shop_name: str,
            shop_location: list[int, int],
            product_list: list[dict]
    ) -> None:
        self.name = shop_name
        self.shop_location = shop_location
        self.product_list = product_list

    def cart_price(self, customer_product_list: dict) -> float:
        return sum(
            (
                customer_product_list[article] * self.product_list[article]
            ) for article in customer_product_list
        )

    @staticmethod
    def define_shop() -> list:
        shops = []
        for shop in shop_list:
            shops.append(Shop(
                shop["name"], shop["location"], shop["products"]
            ))
        return shops

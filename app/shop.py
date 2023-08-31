from app.customer import customers_and_content


class Shop:
    def __init__(
            self, content: dict, name_shop: str,
            product_shop: dict, location_shop: list
    ) -> list:
        self.content = content
        self.name_shop = name_shop
        self.product_shop = product_shop
        self.location_shop = location_shop
        (
            self.location_shop,
            self.name_shop,
            self.product_shop
        ) = self.shop_location_shop()

    def shop_location_shop() -> dict:
        customers, content = customers_and_content()
        shops = content.get("shops")
        location_shop = {}
        name_shop = {}
        product_shop = {}
        count__ = 0
        for elem_ in shops:
            count__ += 1
            name1 = elem_.get("name")
            name_shop.update({count__: name1})
            location_shop1 = elem_.get("location")
            location_shop.update({count__: location_shop1})
            product_shop1 = elem_.get("products")
            product_shop.update({count__: product_shop1})
        return location_shop, name_shop, product_shop

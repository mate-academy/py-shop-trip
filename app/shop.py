from app.customer import customers_and_content


class Shop:
    def __init__(
            self, content: dict) -> list:
        self.content = content

    def shop_location_shop() -> dict:
        customers, content = customers_and_content()
        shops = content.get("shops")
        location_shop = {}
        name_shop = []
        product_shop = {}
        for element in shops:
            name_shop_element = element.get("name")
            name_shop.append(name_shop_element)
            location_shop1 = element.get("location")
            location_shop.update({name_shop_element: location_shop1})
            product_shop1 = element.get("products")
            product_shop.update({name_shop_element: product_shop1})
        return location_shop, name_shop, product_shop

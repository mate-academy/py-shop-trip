from app.customer import customers_and_content


class Shop:
    def __init__(self, content: dict) -> list:
        self.content = content

    def shop_location_shop() -> dict:
        customers, content = customers_and_content()
        shops = content.get("shops")
        location_shop1 = {}
        for elem_ in shops:
            name = elem_.get("name")
            location_shop = elem_.get("location")
            location_shop1.update({name: location_shop})
        return location_shop1

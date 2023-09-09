class Shop:
    def __init__(self, element: dict) -> None:
        self.element = element

    def shop_location(self) -> dict:
        name_shop = self.element.get("name")
        distance_location_shop_x = self.element.get("location")[0]
        distance_location_shop_y = self.element.get("location")[1]
        product = self.element.get("products")
        return {
            "name_shop": name_shop,
            "distance_location_shop_x": distance_location_shop_x,
            "distance_location_shop_y": distance_location_shop_y,
            "product": product
        }

from typing import List, Dict


class Shop:
    def __init__(
            self,
            name_shop: str,
            location: List[int],
            products: Dict[str, int]
    ) -> None:
        self.name_shop = name_shop
        self.location = location
        self.products = products

    def shop_location(self) -> dict:
        return {
            "name_shop": self.name_shop,
            "distance_location_shop_x": self.location[0],
            "distance_location_shop_y": self.location[1],
            "products": self.products
        }

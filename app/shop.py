class Shop:
    def __init__(
            self,
            element: dict,
            name_shop_element: str,
            location_shop_: list,
            product_shop_: dict
    ) -> dict:
        self.element = element
        self.name_shop_element = name_shop_element
        self.location_shop_ = location_shop_
        self.product_shop_ = product_shop_

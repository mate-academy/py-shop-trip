class Shops:
    shops_list = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def add_shop(shops: list):
        shops_list = []
        for shop in shops:
            new_shop = Shops(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            shops_list.append(new_shop)
        return shops_list




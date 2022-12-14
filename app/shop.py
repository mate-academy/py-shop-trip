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

    @staticmethod
    def customer_purchase(
            customer_name: str,
            purchase_note: dict
    ):
        print(
            f"Date: \n"
            f"Thanks, {customer_name}, for you purchase!\n"
            f"You have bought:\n"
            f"{purchase_note['milk']}\n"
            f"{purchase_note['bread']}\n"
            f"{purchase_note['butter']}\n"
            f"Total cost is 26.5 dollars See you again!\n"
            f"\n"
        )



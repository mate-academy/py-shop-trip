class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list,
            money: int
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money

    def money_amount(self) -> str:
        return f"{self.name} has {self.money} dollars\n"

    def cost_of_products_in_shop(self, shop: dict) -> float:
        total_for_shop = 0
        for product in self.products:
            cost_of_product = self.products[product] * shop[product]
            total_for_shop += cost_of_product
        return total_for_shop

    def change_location(self, shop_location: list) -> None:
        self.location = shop_location

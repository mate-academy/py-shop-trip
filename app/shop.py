class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products_price: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products_price = products_price

    def products_cost(self, products_to_buy: dict) -> dict:
        cost_dict = {
            k: v * products_to_buy[k]
            for k, v in self.products_price.items()
            if k in products_to_buy
        }
        return cost_dict

    def sum_cost_of_products(self, products_to_buy: dict) -> float:
        cost_dict = {
            k: v * products_to_buy[k]
            for k, v in self.products_price.items()
            if k in products_to_buy
        }
        return sum(cost_dict.values())

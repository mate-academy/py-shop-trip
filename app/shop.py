class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products_price: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products_price = products_price

    def make_a_bill(self, products_to_buy: dict) -> dict:
        bill = {}
        for product in products_to_buy:
            price = products_to_buy[product] * self.products_price[product]
            if price % 1 == 0:
                bill[product] = int(price)
            else:
                bill[product] = price
        return bill

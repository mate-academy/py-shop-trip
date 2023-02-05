class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money


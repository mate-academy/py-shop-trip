class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(
            self,
            cart: dict
    ) -> dict:
        return {
            product: cart[product] * self.products[product]
            for product in cart
        }

    def shopping(
            self,
            customer_name: str,
            cart: dict,
    ) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        products_cost = self.products_cost(cart)
        for product in products_cost:
            print(f"{cart[product]} {product}s for "
                  f"{self.round_price(products_cost[product])} dollars")

        print(f"Total cost is {sum(self.products_cost(cart).values())}"
              f" dollars")
        print("See you again!\n")

    @staticmethod
    def round_price(price: float) -> int | float:
        if int(price) == price:
            return int(price)
        return price

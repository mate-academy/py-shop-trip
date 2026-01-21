from decimal import Decimal


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = [Decimal(str(x)) for x in location]
        self.products = {
            prod_name: Decimal(str(prod_price))
            for prod_name, prod_price in products.items()
        }

    def get_products_price(self, customer_cart: dict) -> Decimal:
        result = 0
        for customer_key in customer_cart:
            result += self.products[customer_key] * customer_cart[customer_key]

        return Decimal(str(result))

    def bough_info(self, customer_cart: dict) -> None:
        print("You have bought:")
        for customer_key in customer_cart:
            _sum = (self.products[customer_key]
                    * customer_cart[customer_key]
                    ).quantize(Decimal("0.1"))
            if _sum == int(_sum):
                _sum = int(_sum)
            print(f"{customer_cart[customer_key]} "
                  f"{customer_key}s for {_sum} dollars")
        print(f"Total cost is "
              f"{self.get_products_price(customer_cart)} dollars")
        print("See you again!\n")

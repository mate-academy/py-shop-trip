import datetime


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

    def cost_products(self, product_cart: dict) -> float:
        cost = 0

        for product, number in product_cart.items():
            price = self.products[product] * number
            cost += price

        return cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict,
    ) -> None:
        total_cost_of_products = 0
        current_time = datetime.datetime.now()

        print(f"Date: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, number in product_cart.items():
            price = self.products[product] * number
            price = int(price) if (isinstance(price, float)
                                   and price.is_integer()) else price
            print(f"{number} {product}s for {price} dollars")
            total_cost_of_products += price

        print(f"Total cost is {total_cost_of_products} dollars")
        print("See you again!")

import datetime


class Shops:
    def __init__(
            self,
            name: str,
            location: list[int, int],
            products: dict,
    ) -> None:
        self.shop_name = name
        self.shop_location = location
        self.products = products

    def count_price_for_products(
            self,
            customer_product_cart: dict
    ) -> int | float:
        return sum([
            self.products[product_name] * product_count
            for product_name, product_count in customer_product_cart.items()
        ])

    @staticmethod
    def format_price(price: float) -> int | float:
        if int(price) == price:
            price = int(price)
        return price

    def return_products_info(
            self,
            customer_product_cart: dict
    ) -> list:
        return [
            (f"{product_count} {product_name}s for "
             f"{self.format_price(self.products[product_name]*product_count)}"
             f" dollars")
            for product_name, product_count in customer_product_cart.items()
        ]

    def receipt(self, customer_name: str, customer_product_cart: dict) -> None:

        list_of_products = self.return_products_info(customer_product_cart)

        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product in list_of_products:
            print(product)
        print(f"Total cost is "
              f"{self.count_price_for_products(customer_product_cart)}"
              f" dollars")
        print("See you again!\n")
